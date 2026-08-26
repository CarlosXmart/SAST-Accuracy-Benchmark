#!/usr/bin/env python3
import json, os, shutil, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
results=[]
def run(name, cmd, cwd=None, env=None):
    if shutil.which(cmd[0]) is None:
        results.append({'check':name,'status':'SKIP','detail':f'{cmd[0]} not installed'}); return
    p=subprocess.run(cmd,cwd=cwd or ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=env)
    results.append({'check':name,'status':'PASS' if p.returncode==0 else 'FAIL','returncode':p.returncode,'detail':p.stdout[-4000:].replace(str(ROOT),'.')})
(ROOT/'.validation/pycache').mkdir(parents=True,exist_ok=True)
pyenv=os.environ.copy(); pyenv['PYTHONPYCACHEPREFIX']=str(ROOT/'.validation/pycache')
run('python-compileall',['python3','-m','compileall','-q',str(ROOT/'cases/python')],env=pyenv)
java_files=[str(p) for p in (ROOT/'cases/java').rglob('*.java')]
(ROOT/'.validation/java').mkdir(parents=True,exist_ok=True)
run('java-javac',['javac','-Xlint:none','-d',str(ROOT/'.validation/java')]+java_files)
for p in sorted((ROOT/'cases/javascript').rglob('*.js')): run('node-check:'+p.name,['node','--check',str(p)])
run('typescript-tsc',['tsc','-p',str(ROOT/'cases/typescript/tsconfig.json'),'--noEmit'])
run('go-test',['go','test','./...'],cwd=ROOT/'cases/go')
(ROOT/'.validation/c').mkdir(parents=True,exist_ok=True)
for p in sorted((ROOT/'cases/c').rglob('*.c')): run('gcc:'+p.name,['gcc','-std=c11','-D_XOPEN_SOURCE=700','-Wno-deprecated-declarations','-c',str(p),'-o',str(ROOT/'.validation/c'/(p.stem+'.o'))])
(ROOT/'.validation/cpp').mkdir(parents=True,exist_ok=True)
for p in sorted((ROOT/'cases/cpp').rglob('*.cpp')): run('g++:'+p.name,['g++','-std=c++17','-Wno-deprecated-declarations','-c',str(p),'-o',str(ROOT/'.validation/cpp'/(p.stem+'.o'))])
for p in sorted((ROOT/'cases/ruby').rglob('*.rb')): run('ruby-check:'+p.name,['ruby','-c',str(p)])
for p in sorted((ROOT/'cases/php').rglob('*.php')): run('php-lint:'+p.name,['php','-l',str(p)])
def balanced_source(path):
    text=path.read_text(encoding='utf-8'); pairs={')':'(',']':'[','}':'{'}; stack=[]; quote=None; esc=False; i=0
    while i < len(text):
        ch=text[i]; nxt=text[i+1] if i+1 < len(text) else ''
        if quote:
            if esc: esc=False
            elif ch=='\\': esc=True
            elif ch==quote: quote=None
            i+=1; continue
        if ch in ('"', "'"): quote=ch; i+=1; continue
        if ch=='/' and nxt=='/':
            j=text.find('\n',i); i=len(text) if j<0 else j+1; continue
        if ch=='/' and nxt=='*':
            j=text.find('*/',i+2)
            if j<0: return False, 'unterminated block comment'
            i=j+2; continue
        if ch=='#' and path.suffix=='.tf':
            j=text.find('\n',i); i=len(text) if j<0 else j+1; continue
        if ch in '([{': stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop()!=pairs[ch]: return False, f'unbalanced token {ch}'
        i+=1
    if quote: return False, 'unterminated string'
    if stack: return False, 'unclosed delimiters'
    return True, 'balanced delimiters/strings/comments'
for pth in sorted((ROOT/'cases/csharp').rglob('*.cs')):
    ok,detail=balanced_source(pth); results.append({'check':'csharp-structural:'+pth.name,'status':'PASS' if ok else 'FAIL','detail':detail})
if shutil.which('dotnet'): results.append({'check':'csharp-compiler','status':'INFO','detail':'dotnet present; external SqlClient package restore is intentionally not performed.'})
else: results.append({'check':'csharp-compiler','status':'SKIP','detail':'dotnet/Roslyn not installed; C# received structural + manual review.'})
for pth in sorted((ROOT/'cases/terraform').rglob('*.tf')):
    ok,detail=balanced_source(pth); results.append({'check':'terraform-structural:'+pth.name,'status':'PASS' if ok else 'FAIL','detail':detail})
if shutil.which('terraform'):
    for pth in sorted((ROOT/'cases/terraform').rglob('*.tf')): run('terraform-fmt:'+pth.name,['terraform','fmt','-check',str(pth)])
else: results.append({'check':'terraform-fmt','status':'SKIP','detail':'terraform binary not installed; HCL received structural + manual review.'})
failed=[r for r in results if r['status']=='FAIL']
report={'summary':{'checks':len(results),'pass':sum(r['status']=='PASS' for r in results),'skip':sum(r['status']=='SKIP' for r in results),'fail':len(failed)},'results':results}
out=ROOT/'benchmark_meta'/'validation_report.json'; out.write_text(json.dumps(report,indent=2),encoding='utf-8'); print(json.dumps(report['summary'],indent=2))
if failed:
    for f in failed: print('\nFAILED',f['check'],'\n',f['detail'])
    sys.exit(1)
