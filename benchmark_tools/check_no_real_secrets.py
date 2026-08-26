#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
patterns=[r'AKIA[0-9A-Z]{16}', r'-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----', r'gh[pousr]_[A-Za-z0-9]{30,}', r'sk-[A-Za-z0-9]{20,}']
errors=[]
for p in ROOT.rglob('*'):
    if p.is_file() and '.validation' not in p.parts:
        try: txt=p.read_text(errors='ignore')
        except: continue
        for pat in patterns:
            if re.search(pat,txt): errors.append(f'{p.relative_to(ROOT)} matches {pat}')
print(f'secret-pattern-errors={len(errors)}')
for e in errors: print(e)
sys.exit(1 if errors else 0)
