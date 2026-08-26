# Pipeline XGuardian SAST

## Objetivo

Executar o corpus deste repositório pelo fluxo oficial do XGuardian sem misturar ground truth, scripts de avaliação ou arquivos de CI no alvo do SAST.

## Contrato utilizado

A pipeline referencia de forma imutável:

```text
xmart-xguardian/xguardian-actions@8854a4b1ae87beada624979c8dd26d985bdf7957
```

Esse SHA corresponde ao HEAD observado da release documentada como `v25.3.0` durante a configuração do benchmark.

## Configuração obrigatória

Em **Settings → Secrets and variables → Actions**:

### Repository Secrets

- `API_EMAIL` — conta técnica/autorizada do XGuardian.
- `API_PASSWORD` — senha correspondente.

Nunca versione essas credenciais no repositório.

### Repository Variables

- `XGUARDIAN_TEAM_ID` — array JSON com o(s) ID(s) real(is) da equipe de benchmark. Ex.: `[123]`.
- `XGUARDIAN_LANGUAGES` — array JSON com os nomes de linguagem aceitos pelo XGuardian para a aplicação.
- `XGUARDIAN_PIPELINE_ENABLED` — opcional. Use `true` para permitir scans automáticos em pushes de `main`.

Não existe fallback para `team_id=1`. Isso é intencional para evitar associação incorreta entre organização/equipe.

## O que entra no scan

A Action recebe `scan_directory: "."`, mas o campo `exclude` remove:

```text
benchmark_meta
benchmark_tools
.github
cases/typescript/tsconfig.json
```

Dessa forma, o ZIP montado pela Action mantém apenas o corpus que deve ser pontuado. O `tsconfig.json` é usado para validação de TypeScript, mas não pertence à massa do scanner e poderia ser tratado como IaC/JSON pelo engine.

## Baseline da execução

- SAST: `true`
- SCA: `false`
- DAST: `false`
- `policy_sast: 0`
- `translate: false`
- `pdf: false`
- `save_vulns: true`
- `get_scan_id: true`
- ambiente manual padrão: `development`

A política fica em `0` porque o corpus contém vulnerabilidades de propósito. Um quality gate que derrubasse a execução por encontrar vulnerabilidades invalidaria o objetivo do benchmark.

## Execução manual

1. Configure os Secrets e Variables acima.
2. Abra **Actions → XGuardian SAST Accuracy Benchmark**.
3. Clique em **Run workflow**.
4. Escolha `development` ou `production`.

Use `development` para ensaio e validação, salvo necessidade explícita de medir produção.

## Execução automática

Defina:

```text
XGUARDIAN_PIPELINE_ENABLED=true
```

A partir daí, mudanças relevantes em `cases/**`, ground truth ou no workflow, quando integradas em `main`, podem disparar novo scan.

Sem essa variável, pushes não consomem scan.

## Resultado

A Action fornece `app_id`, `scan_id`, `scan_url` e `scan_version`. O workflow publica esses dados no **GitHub Job Summary**.

Após obter o JSON final do SAST:

```bash
python3 benchmark_tools/evaluate_xguardian.py result.json --output-dir benchmark_score
```

## Rastreabilidade

Para cada execução relevante, registre junto ao score:

- commit do benchmark;
- `scan_id` e `scan_version`;
- ambiente;
- SHA da XGuardian Action;
- engine/scanners/rules observados;
- configuração de excludes/política/filtros;
- falhas parciais, se houver.

Não compare resultados de configurações diferentes como regressão ou evolução direta.

## Risco conhecido da Action atual

A implementação atual da Action possui um step que imprime os valores recebidos de email/senha. GitHub Actions normalmente mascara valores originados de Secrets, mas isso continua sendo uma prática inadequada na Action e deve ser removida em evolução própria do `xguardian-actions`.

Este repositório não registra nem imprime diretamente essas credenciais.
