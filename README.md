# XGuardian SAST Accuracy Benchmark

Benchmark controlado e poliglota para medir a acurácia do pipeline **SAST efetivo do XGuardian**.

> **Segurança:** este repositório contém vulnerabilidades intencionais. Ele existe exclusivamente para análise estática. Não publique, execute ou implante os casos vulneráveis como aplicação real.

## Escopo v1

- **164 casos controlados**
- **82 vulnerabilidades reais intencionais (positivos)**
- **82 casos benignos / hard-negatives (negativos)**
- **26 CWEs-alvo**
- C, C++, C#, Go, Java, JavaScript, PHP, Python, Ruby, TypeScript e Terraform
- track `core` para código tradicional e track `iac` para Terraform

Cada caso vive em um arquivo isolado e possui marcadores `XG-BENCH:<ID> START/END`. Isso permite matching determinístico entre o finding do XGuardian e o ground truth.

## Estrutura

```text
.github/workflows/
  benchmark-validation.yml   # valida integridade sem disparar scan
  xguardian-sast.yml         # executa o SAST no XGuardian
cases/
  <language>/positive/       # vulnerabilidades intencionais
  <language>/negative/       # hard-negatives / honeypots seguros
benchmark_meta/
  ground_truth.full.json.gz  # catálogo completo e revisado dos 164 casos
  methodology.md
  expected_counts.json
  xguardian_baseline.md
  references.md
  runbook.md
benchmark_tools/
  check_ground_truth.py
  check_no_real_secrets.py
  validate_suite.py
  evaluate_xguardian.py
PIPELINE.md
```

## Ground truth

`benchmark_meta/ground_truth.full.json.gz` contém o catálogo completo de cada caso: ID, linguagem, caminho, expectativa vulnerável/benigna, CWE alvo e aceitos, categoria, variante, complexidade, track, linhas e racional.

Validação rápida:

```bash
python3 benchmark_tools/check_ground_truth.py
python3 benchmark_tools/check_no_real_secrets.py
```

Validação ampla das toolchains disponíveis:

```bash
python3 benchmark_tools/validate_suite.py
```

A baseline original deste corpus resultou em **96 PASS / 2 SKIP / 0 FAIL**. Os SKIPs eram ausência de toolchain de compilação C# e do binário Terraform no ambiente de validação; não foram apresentados como PASS.

## Pipeline XGuardian

O workflow `.github/workflows/xguardian-sast.yml` usa a Action SAST oficial:

```text
xguardian-actions/actions/sast@6373d9375d3a859f602dcf53b37a3d8326c8a248
```

O SHA corresponde à release `v26.6.2`.

### Massa analisada

O XGuardian recebe **somente `cases/`**:

```yaml
scan_directory: "cases"
```

Arquivos fora de `cases/` — documentação, ground truth, tooling e workflows — não entram no ZIP da Action.

`cases/typescript/tsconfig.json` é removido somente do checkout temporário do runner antes do scan, porque serve para validação local e não pertence aos 164 casos pontuados. `cases/go/go.mod` permanece como contexto auxiliar do track Go.

### Configuração da aplicação

O benchmark usa uma aplicação existente por `XGUARDIAN_APP_ID`. Dessa forma, `languages`, `team_id` e `app_name` não precisam ser enviados pela pipeline.

Isso também evita que o default de `languages` da Action (`["JavaScript"]`) gere metadata incorreta para um corpus poliglota.

Configuração necessária:

```text
Secret:
XGUARDIAN_TOKEN

Variable:
XGUARDIAN_APP_ID
```

Execução automática em `push` só acontece quando `XGUARDIAN_PIPELINE_ENABLED=true` estiver configurado.

Veja [PIPELINE.md](PIPELINE.md) para detalhes operacionais.

## Avaliação do resultado

Após exportar o resultado SAST do XGuardian em JSON:

```bash
python3 benchmark_tools/evaluate_xguardian.py result.json --output-dir benchmark_score
```

O avaliador aceita:

- export JSON do XGuardian com `arquivo` / `linha` / `cwe`;
- resultado SARIF-like do engine;
- JSON bruto do Semgrep.

Ele gera:

- `score.json`
- `case_results.csv`
- `unmatched_findings.json`
- `extraneous_findings.json`

## Métricas

O benchmark calcula **TP, TN, FP, FN, Precision, Recall/TPR, FPR, Specificity, F1, Accuracy, Balanced Accuracy, MCC, OWASP-style score e Taxonomy Accuracy**, com breakdown geral, por track, linguagem e CWE.

Não use `accuracy` isoladamente. Para SAST, principalmente, **Precision + Recall + FPR** explicam muito melhor a qualidade do scanner.

## Regra de comparação

Um score só é comparável com outro quando permanecem registrados e controlados:

- commit do benchmark;
- endpoint/ambiente efetivo usado pela Action;
- commit/versão do engine;
- versão/imagem dos scanners;
- packs/custom rules;
- filtros/conditional audits e pós-processamento.

Acurácia não é uma constante do produto; é resultado de **corpus + versão + configuração + pipeline**.
