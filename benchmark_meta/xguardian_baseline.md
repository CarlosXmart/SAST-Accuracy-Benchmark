# XGuardian SAST baseline used by this benchmark

**Reference date:** 2026-08-26  
**Repository checked:** `xmart-xguardian/xguardian-engine`  
**Production/main commit observed:** `758cd943fcd2a6ceeeecea6f4848a96190cafd55`

## Confirmed behavior

- O engine executa um passe centralizado do Semgrep antes dos analyzers específicos.
- O runner central usa packs baseline, security audit/CWE/OWASP e packs por linguagem.
- O estado observado referencia Semgrep `1.99.0` e custom rules XGuardian para Java/JavaScript.
- O mapeamento específico inclui, entre outros, Bandit/Python, GoSec/Go, Flawfinder/C/C++ e Brakeman/Ruby.
- Findings são normalizados e posteriormente deduplicados.

## Escopo

Este benchmark mede a **saída efetiva do pipeline SAST do XGuardian**. Não publique o resultado como score de um scanner upstream isolado sem executar e pontuar esse scanner separadamente.
