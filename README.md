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

O arquivo está comprimido apenas para reduzir ruído/tamanho no Git. Os validadores e o avaliador o leem diretamente; não há perda semântica.

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

O workflow `.github/workflows/xguardian-sast.yml` usa a Action SAST oficial publicada em:

```text
xguardian-actions/actions/sast
```

Para reprodutibilidade, o benchmark fixa a release `v26.6.2` pelo commit:

```text
xguardian-actions/actions/sast@6373d9375d3a859f602dcf53b37a3d8326c8a248
```

A autenticação usa o PAT `XGUARDIAN_TOKEN`, conforme o contrato atual da Action oficial. O workflow também exige `XGUARDIAN_TEAM_ID` e `XGUARDIAN_LANGUAGES` como Repository Variables.

O scan é **SAST-only**. A lista `exclude` solicita ao XGuardian que `benchmark_meta`, `benchmark_tools`, `.github` e `cases/typescript/tsconfig.json` não participem da análise pontuada. A efetividade desse filtro deve ser validada no primeiro resultado do scan.

A Action SAST específica `v26.6.2` utiliza os endpoints de **produção** do XGuardian e não expõe seletor `development/production`.

Execução automática em `push` só acontece quando `XGUARDIAN_PIPELINE_ENABLED=true` estiver configurado no repositório.

Veja [PIPELINE.md](PIPELINE.md) para configuração de Secrets/Variables e operação.

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
- exclusões;
- filtros/conditional audits e pós-processamento.

Acurácia não é uma constante do produto; é resultado de **corpus + versão + configuração + pipeline**.
