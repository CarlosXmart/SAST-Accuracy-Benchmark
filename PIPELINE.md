# Pipeline do XGuardian

Este repositório possui o workflow `.github/workflows/xguardian-sast.yml` para executar o corpus controlado no SAST do XGuardian.

## Princípio do benchmark

O workflow escaneia o repositório, mas remove explicitamente da massa do scanner:

- `benchmark_meta/` — ground truth, hashes e documentação;
- `benchmark_tools/` — avaliador/validadores Python;
- `.github/` — workflow CI;
- `cases/typescript/tsconfig.json` — arquivo de validação TypeScript que não pertence ao payload de SAST e poderia ser classificado como IaC.

Assim, os caminhos dos casos permanecem `cases/<linguagem>/...`, iguais aos registrados no ground truth.

## Configuração obrigatória no GitHub

Em **Settings → Secrets and variables → Actions**, configure:

### Secrets

- `API_EMAIL` — conta técnica/autorizada do XGuardian.
- `API_PASSWORD` — senha correspondente.

Nunca versione essas credenciais no repositório.

### Repository variables

- `XGUARDIAN_TEAM_ID` — array JSON com o(s) ID(s) real(is) da equipe responsável pela aplicação de benchmark, por exemplo `[123]`.
- `XGUARDIAN_LANGUAGES` — array JSON com os nomes de linguagem aceitos pela organização/aplicação no XGuardian.
- `XGUARDIAN_PIPELINE_ENABLED` — defina como `true` somente quando quiser scans automáticos em `push` para `main`.

`XGUARDIAN_TEAM_ID` não possui fallback proposital. O benchmark não assume `team_id=1`, evitando associação incorreta entre tenants/equipes.

## Execução

### Manual

1. Abra **Actions**.
2. Selecione **XGuardian SAST Accuracy Benchmark**.
3. Clique em **Run workflow**.
4. Escolha `development` ou `production`.

O padrão é `development`.

### Automática

Defina `XGUARDIAN_PIPELINE_ENABLED=true`. O workflow passa a executar em pushes para `main` quando houver mudança em `cases/**`, no ground truth ou no próprio workflow.

## Baseline de scan

O workflow executa somente SAST:

- `sast: true`;
- `sca: false`;
- `dast: false`;
- `policy_sast: 0`;
- `translate: false`;
- `pdf: false`;
- `save_vulns: true`;
- `get_scan_id: true`.

A política SAST fica em `0` de propósito. O corpus contém vulnerabilidades intencionais; um quality gate que falhasse ao encontrar vulnerabilidades tornaria o benchmark inutilizável. A métrica correta é calculada contra o ground truth.

## Action fixada

Para reprodutibilidade, o workflow referencia o commit:

`xmart-xguardian/xguardian-actions@8854a4b1ae87beada624979c8dd26d985bdf7957`

Esse commit corresponde ao HEAD atual da release documentada como `v25.3.0` quando o repositório foi configurado.

Atualizações da Action devem ser feitas de forma explícita, registrando o novo SHA junto ao resultado do benchmark.

## Resultado e cálculo de acurácia

A Action fornece `app_id`, `scan_id`, `scan_url` e `scan_version`; o workflow os publica no Job Summary.

Depois que o resultado SAST for exportado em JSON, execute:

```bash
python3 benchmark_tools/evaluate_xguardian.py result.json --output-dir benchmark_score
```

Os principais artefatos serão:

- `benchmark_score/score.json`;
- `benchmark_score/case_results.csv`;
- `benchmark_score/unmatched_findings.json`;
- `benchmark_score/extraneous_findings.json`.

Não compare scores de execuções com versões de Action, engine, rules, políticas, excludes ou ambientes diferentes sem registrar a diferença.
