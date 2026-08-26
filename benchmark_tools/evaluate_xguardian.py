#!/usr/bin/env python3
import argparse, csv, gzip, json, math, os, re
from pathlib import Path
from collections import defaultdict

def norm_path(v):
    v = str(v or '').replace('\\','/').strip()
    while v.startswith('./'): v=v[2:]
    return v

def norm_cwe(v):
    if v is None: return None
    m=re.search(r'CWE[-_ ]?(\d+)', str(v), re.I)
    return f'CWE-{m.group(1)}' if m else str(v).upper().strip()

def recursively_find_export_findings(obj, out):
    if isinstance(obj, dict):
        if 'arquivo' in obj and ('linha' in obj or 'cwe' in obj):
            out.append({'path':obj.get('arquivo'),'line':obj.get('linha'),'cwe':obj.get('cwe'),'tool':obj.get('tool') or 'XGuardian','language':obj.get('linguagem'),'raw':obj})
        for v in obj.values(): recursively_find_export_findings(v,out)
    elif isinstance(obj,list):
        for v in obj: recursively_find_export_findings(v,out)

def parse_findings(path):
    data=json.loads(Path(path).read_text(encoding='utf-8'))
    out=[]
    if isinstance(data,dict) and isinstance(data.get('runs'),list):
        for run in data['runs']:
            for r in run.get('results',[]):
                locs=r.get('locations') or []
                phys=(locs[-1].get('physicalLocation',{}) if locs else {})
                out.append({'path':phys.get('artifactLocation',{}).get('uri'),'line':phys.get('region',{}).get('startLine'),'cwe':r.get('ruleId'),'tool':r.get('properties',{}).get('tool'),'language':r.get('properties',{}).get('language'),'raw':r})
    if isinstance(data,dict) and isinstance(data.get('results'),list) and any(isinstance(x,dict) and 'extra' in x for x in data['results']):
        for r in data['results']:
            meta=r.get('extra',{}).get('metadata',{}); cwe=meta.get('cwe')
            if isinstance(cwe,list): cwe=cwe[0] if cwe else None
            out.append({'path':r.get('path'),'line':r.get('start',{}).get('line'),'cwe':cwe,'tool':'semgrep','language':None,'raw':r})
    recursive=[]; recursively_find_export_findings(data, recursive)
    seen=set(); merged=[]
    for f in out+recursive:
        key=(norm_path(f.get('path')),f.get('line'),norm_cwe(f.get('cwe')),str(f.get('tool')))
        if key in seen: continue
        seen.add(key); f['path']=norm_path(f.get('path')); f['cwe']=norm_cwe(f.get('cwe')); merged.append(f)
    return merged

def load_cases(manifest_path):
    p=Path(manifest_path)
    if p.suffix == '.gz':
        with gzip.open(p, 'rt', encoding='utf-8') as fh: data=json.load(fh)
    else:
        data=json.loads(p.read_text(encoding='utf-8'))
    return data['cases']

def path_case(fpath, cases):
    matches=[]
    for c in cases:
        cp=norm_path(c['path'])
        if fpath == cp or fpath.endswith('/'+cp) or fpath.endswith(cp): matches.append(c)
    return max(matches, key=lambda c:len(c['path'])) if matches else None

def div(a,b): return a/b if b else 0.0

def metrics(rows):
    tp=sum(r['outcome']=='TP' for r in rows); fn=sum(r['outcome']=='FN' for r in rows)
    tn=sum(r['outcome']=='TN' for r in rows); fp=sum(r['outcome']=='FP' for r in rows)
    tpr=div(tp,tp+fn); fpr=div(fp,fp+tn); precision=div(tp,tp+fp); specificity=div(tn,tn+fp)
    f1=div(2*precision*tpr,precision+tpr); accuracy=div(tp+tn,tp+tn+fp+fn); balanced=(tpr+specificity)/2
    denom=math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn)); mcc=((tp*tn)-(fp*fn))/denom if denom else 0.0
    return {'TP':tp,'FN':fn,'TN':tn,'FP':fp,'precision':precision,'recall_tpr':tpr,'false_positive_rate':fpr,'specificity':specificity,'f1':f1,'accuracy':accuracy,'balanced_accuracy':balanced,'mcc':mcc,'owasp_style_score':100*(tpr-fpr)}

def main():
    ap=argparse.ArgumentParser(description='Score XGuardian SAST findings against XG benchmark ground truth.')
    ap.add_argument('report', help='XGuardian JSON / engine SARIF-like JSON / raw Semgrep JSON')
    ap.add_argument('--manifest', default=str(Path(__file__).resolve().parents[1]/'benchmark_meta'/'ground_truth.full.json.gz'))
    ap.add_argument('--line-tolerance', type=int, default=3); ap.add_argument('--output-dir', default='benchmark_score')
    args=ap.parse_args(); cases=load_cases(args.manifest); findings=parse_findings(args.report)
    mapped=defaultdict(list); unmatched=[]
    for f in findings:
        c=path_case(norm_path(f.get('path')),cases)
        if c: mapped[c['id']].append(f)
        else: unmatched.append(f)
    rows=[]; taxonomy_ok=taxonomy_total=0; extraneous=[]
    for c in cases:
        fs=mapped.get(c['id'],[]); in_range=[]
        for f in fs:
            try: line=int(f.get('line'))
            except (TypeError,ValueError): line=None
            if line is None or (c['start_line']-args.line_tolerance <= line <= c['end_line']+args.line_tolerance): in_range.append(f)
        detected=bool(in_range)
        if c['expected_vulnerable']:
            outcome='TP' if detected else 'FN'
            for f in fs:
                try: fl=int(f.get('line'))
                except (TypeError,ValueError): fl=None
                if fl is not None and not (c['start_line']-args.line_tolerance <= fl <= c['end_line']+args.line_tolerance): extraneous.append({'case_id':c['id'], **{k:v for k,v in f.items() if k!='raw'}})
            if detected:
                taxonomy_total += 1; accepted={norm_cwe(x) for x in c['allowed_cwes']}
                if any(norm_cwe(f.get('cwe')) in accepted for f in in_range): taxonomy_ok += 1
        else:
            detected=bool(fs); outcome='FP' if detected else 'TN'
        rows.append({**c,'outcome':outcome,'finding_count':len(fs),'in_range_finding_count':len(in_range),'observed_cwes':sorted({f.get('cwe') for f in fs if f.get('cwe')})})
    overall=metrics(rows); overall['taxonomy_accuracy_on_tp']=div(taxonomy_ok,taxonomy_total); overall['taxonomy_correct_tp']=taxonomy_ok; overall['taxonomy_evaluated_tp']=taxonomy_total; overall['total_input_findings']=len(findings); overall['unmatched_findings']=len(unmatched); overall['extraneous_findings_on_positive_files']=len(extraneous)
    by_track={track:metrics([r for r in rows if r.get('track','core')==track]) for track in sorted({r.get('track','core') for r in rows})}
    by_language={lang:metrics([r for r in rows if r['language']==lang]) for lang in sorted({r['language'] for r in rows})}
    by_cwe={cwe:metrics([r for r in rows if r['target_cwe']==cwe]) for cwe in sorted({r['target_cwe'] for r in rows})}
    outdir=Path(args.output_dir); outdir.mkdir(parents=True,exist_ok=True)
    (outdir/'score.json').write_text(json.dumps({'overall':overall,'by_track':by_track,'by_language':by_language,'by_cwe':by_cwe},indent=2),encoding='utf-8')
    with (outdir/'case_results.csv').open('w',newline='',encoding='utf-8') as fh:
        keys=['id','language','path','expected_vulnerable','target_cwe','category','variant','complexity','outcome','finding_count','in_range_finding_count','observed_cwes']; w=csv.DictWriter(fh,fieldnames=keys); w.writeheader()
        for r in rows:
            rr={k:r[k] for k in keys}; rr['observed_cwes']='|'.join(rr['observed_cwes']); w.writerow(rr)
    (outdir/'unmatched_findings.json').write_text(json.dumps([{k:v for k,v in f.items() if k!='raw'} for f in unmatched],indent=2,ensure_ascii=False),encoding='utf-8')
    (outdir/'extraneous_findings.json').write_text(json.dumps(extraneous,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps(overall, indent=2)); print(f'Wrote: {outdir}/score.json, case_results.csv, unmatched_findings.json, extraneous_findings.json')
if __name__=='__main__': main()
