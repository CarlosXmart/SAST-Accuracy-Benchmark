# Referências e baseline técnico

## XGuardian

O desenho foi alinhado ao `xmart-xguardian/xguardian-engine`, branch `main`, commit observado `758cd943fcd2a6ceeeecea6f4848a96190cafd55`.

Foram considerados `scanner.py`, runner/formatter do Semgrep, analyzers específicos, `extensions.py` e `report-editor.py`. O benchmark mede a **saída efetiva do XGuardian**, não a acurácia isolada de um único motor.

## Histórico interno considerado

Análises anteriores evidenciaram ruído em famílias como CWE-532, CWE-89, CWE-611, CWE-321, CWE-327 e CWE-918. O corpus inclui hard-negatives nessas fronteiras sem ajustar artificialmente o resultado esperado ao scanner.

## Referências externas

- OWASP Benchmark: https://owasp.org/www-project-benchmark/
- NIST SARD / Juliet Test Suite: https://samate.nist.gov/SARD/
- CWE: https://cwe.mitre.org/
