# XGuardian SAST Accuracy Benchmark v1.0

Benchmark poliglota controlado para medir **precisão, recall, taxa de falsos positivos, discriminação e coerência de CWE** do pipeline SAST do XGuardian.

> **NÃO implante nem execute os trechos vulneráveis.** Eles existem exclusivamente como massa estática de scanner. A validação incluída compila/analisa sintaxe quando a toolchain está disponível, sem chamar funções vulneráveis.

## Escopo

- **164 casos catalogados**
- **82 vulneráveis intencionais**
- **82 benignos/hard-negatives**
- **26 CWEs-alvo**
- Linguagens/trilhas: C, C++, C#, Go, Java, JavaScript, PHP, Python, Ruby, Terraform e TypeScript
- `core`: código-fonte tradicional
- `iac`: Terraform, reportado separadamente para não mascarar a acurácia do SAST de código
- Ground truth: `benchmark_meta/ground_truth.json` e `benchmark_meta/ground_truth.csv`
- Avaliador: `benchmark_tools/evaluate_xguardian.py`
- Validador: `benchmark_tools/validate_suite.py`

## Artefatos de entrega

Há dois artefatos distintos por desenho:

1. **`xguardian-sast-accuracy-scan-payload-v1.zip`** — é o único ZIP que deve ser enviado ao XGuardian. Contém apenas os casos a serem escaneados.
2. **`xguardian-sast-accuracy-benchmark-v1.zip`** — kit de avaliação, ground truth, metodologia, validadores e cópia auditável dos casos. **Não use este ZIP como entrada do scan**, pois scripts e metadados do próprio benchmark contaminariam a medição.

O `tsconfig.json` usado para validar TypeScript existe somente no kit completo e não no payload de scan, evitando que um JSON de build seja interpretado como IaC pelo pipeline atual.

## Como medir o XGuardian

1. Crie uma aplicação de benchmark dedicada e isolada de código de cliente.
2. Envie **somente `xguardian-sast-accuracy-scan-payload-v1.zip`** para um scan SAST.
3. Não altere regras, exclusões, conditional audits ou pós-processamento em relação ao baseline que deseja medir.
4. Registre o commit/versão/configuração efetiva do XGuardian e dos scanners.
5. Preserve o resultado original do scan e exporte o SAST em JSON.
6. No kit completo, execute:

```bash
python3 benchmark_tools/evaluate_xguardian.py /caminho/resultado-xguardian.json --output-dir benchmark_score
```

7. Consulte:
   - `benchmark_score/score.json`
   - `benchmark_score/case_results.csv`
   - `benchmark_score/unmatched_findings.json`
   - `benchmark_score/extraneous_findings.json`

## Métricas

Não use `accuracy` isoladamente.

- **Precision / PPV** = `TP / (TP + FP)` — quanto do que foi acusado nos casos controlados é realmente vulnerável.
- **Recall / TPR** = `TP / (TP + FN)` — quanto das vulnerabilidades reais foi encontrado.
- **FPR** = `FP / (FP + TN)` — quanto dos hard-negatives foi acusado indevidamente.
- **Specificity** = `TN / (TN + FP)`.
- **F1** — equilíbrio entre precision e recall.
- **Balanced Accuracy** — média de TPR e specificity.
- **MCC** — correlação da matriz de confusão, útil mesmo com distribuição desigual em recortes.
- **OWASP-style score** = `100 × (TPR − FPR)`.
- **Taxonomy accuracy** — percentual de TPs cujo CWE reportado pertence ao conjunto aceito pelo caso.

O `score.json` traz resultado **overall**, por **track** (`core` e `iac`), por linguagem e por CWE.

## O que é um falso positivo neste corpus

Um arquivo em `negative/` é deliberadamente benigno, mas desenhado para se parecer com um padrão vulnerável: SQL parametrizado, comando constante, URL allowlisted, parser XML endurecido, validação de origin, bounds check, API segura, segredo sintético em fixture, logging não sensível etc.

**Qualquer finding em um arquivo benigno conta como FP no nível de caso.** Isso evita “perdoar” uma regra apenas porque ela apontou outra linha do mesmo honeypot.

Em arquivos positivos, findings claramente fora do intervalo anotado são preservados em `extraneous_findings.json` para revisão e não são silenciosamente usados para transformar um FN em TP.

## Reprodutibilidade

Para comparar versões do XGuardian, mantenha iguais:

- hash do payload;
- exclusões;
- branch/commit do engine;
- imagem/versão de scanner;
- packs e custom rules;
- modo de scan;
- conditional audits/filtros;
- formato de resultado usado pelo avaliador.

Nunca compare dois scores obtidos com configurações diferentes como se fossem regressão/evolução do scanner.

## Estrutura

```text
cases/<linguagem>/positive/   # vulnerabilidades reais intencionais
cases/<linguagem>/negative/   # hard-negatives / honeypots seguros
benchmark_meta/               # ground truth, metodologia, baseline, hashes e validações
benchmark_tools/              # avaliação e verificações locais
```

## Critério de aceite do benchmark

Antes de uso:

```bash
python3 benchmark_tools/check_ground_truth.py
python3 benchmark_tools/check_no_real_secrets.py
python3 benchmark_tools/validate_suite.py
```

O pacote é aceitável quando:

- ground truth retorna zero inconsistências;
- nenhum padrão de segredo real é encontrado;
- o validador apresenta `FAIL = 0`;
- qualquer `SKIP` por toolchain indisponível está explicitamente documentado;
- o self-test do avaliador confirma matrizes perfeita, tudo-detectado e nada-detectado.

## Limite importante

Este pacote define a verdade conhecida. **Ele não contém nem inventa um percentual de acurácia do XGuardian.** TP/FP/FN/TN, precision, recall e F1 só existem depois que a versão/configuração real do XGuardian for executada contra o payload.
