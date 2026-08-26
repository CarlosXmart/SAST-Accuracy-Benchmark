#!/usr/bin/env python3
import gzip, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
with gzip.open(ROOT/'benchmark_meta/ground_truth.full.json.gz','rt',encoding='utf-8') as fh:
    data=json.load(fh)
errors=[]; seen=set()
for c in data['cases']:
    if c['id'] in seen: errors.append(f"duplicate id {c['id']}")
    seen.add(c['id'])
    p=ROOT/c['path']
    if not p.exists(): errors.append(f"missing {c['path']}"); continue
    lines=p.read_text(errors='replace').splitlines()
    if c['start_line']<1 or c['end_line']>len(lines) or c['start_line']>c['end_line']: errors.append(f"bad range {c['id']}")
    marker=f"XG-BENCH:{c['id']}"
    if sum(marker in x for x in lines)!=2: errors.append(f"marker count {c['id']}")
print(f"cases={len(data['cases'])} errors={len(errors)}")
for e in errors: print(e)
sys.exit(1 if errors else 0)
