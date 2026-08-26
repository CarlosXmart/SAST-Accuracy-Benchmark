# Runbook de medição XGuardian

## Pré-condições

Use uma aplicação de benchmark dedicada. Não misture o corpus com repositórios de cliente e não execute os trechos vulneráveis.

Registre data/hora, ambiente, branch/commit do engine, versão dos scanners quando observável, exclusões, filtros/conditional audits, commit do corpus, status final e qualquer falha parcial de scanner.

## Execução

1. Rode SAST com a configuração que deseja avaliar.
2. Não adicione exclusões para melhorar artificialmente o score.
3. Preserve logs/artefatos sanitizados e o JSON final sem edição manual.
4. Calcule o score:

```bash
python3 benchmark_tools/evaluate_xguardian.py resultado.json --output-dir benchmark_score
```

O avaliador produz TP/FN/TN/FP, Precision, Recall, FPR, Specificity, F1, Balanced Accuracy, MCC, score OWASP-style, breakdown por track/linguagem/CWE, taxonomy accuracy, unmatched findings e findings extraneous.

## Regressões

Rastreie cada FP/FN relevante do finding final para scanner/regra original, output bruto, formatter, deduplicação e pós-processamento. Não atribua automaticamente o erro ao scanner primário.
