# Pipeline XGuardian SAST

## Objetivo

Executar o corpus deste repositório pelo fluxo oficial do XGuardian usando a Action SAST publicada em `xguardian-actions/actions`, sem tratar ground truth, tooling de avaliação ou arquivos de CI como parte da medição.

## Referência oficial

A referência funcional da pipeline é:

```text
xguardian-actions/actions/sast
```

O benchmark fixa a release `v26.6.2` pelo SHA imutável:

```text
xguardian-actions/actions/sast@6373d9375d3a859f602dcf53b37a3d8326c8a248
```

Isso evita que alterações futuras em `main` mudem silenciosamente o comportamento de uma execução histórica do benchmark.

## Autenticação

A Action SAST atual autentica por **PAT (Personal Access Token)** do XGuardian.

Em **Settings → Secrets and variables → Actions** configure:

### Repository Secrets

- `XGUARDIAN_TOKEN` — PAT gerado na plataforma XGuardian.

Nunca versione o token no repositório.

### Repository Variables

- `XGUARDIAN_TEAM_ID` — array JSON com o(s) ID(s) real(is) da equipe de benchmark. Ex.: `[123]`.
- `XGUARDIAN_LANGUAGES` — array JSON com os nomes de linguagem aceitos pelo XGuardian para a aplicação.
- `XGUARDIAN_PIPELINE_ENABLED` — opcional. Use `true` para permitir scans automáticos em pushes de `main`.

Não existe fallback local para `team_id=1`; o workflow exige configuração explícita para evitar associação indevida de equipe.

## Configuração do scan

A pipeline usa:

```text
scan_directory: "."
translate: "false"
pdf: "false"
get_scan_id: "true"
```

A Action dedicada `sast/` já cria uma requisição SAST com `sast=true` e `sca=false`; portanto o workflow não replica flags de outros tipos de scan.

O campo `exclude` enviado ao XGuardian contém:

```text
benchmark_meta/
benchmark_tools/
.github/
cases/typescript/tsconfig.json
```

Importante: a implementação atual da Action cria o ZIP do diretório informado e encaminha `exclude` no payload de criação do scan. Portanto, a exclusão efetiva desses caminhos deve ser confirmada no primeiro resultado do XGuardian; o benchmark não assume silenciosamente que os arquivos foram removidos fisicamente do ZIP.

## Ambiente

A Action específica `xguardian-actions/actions/sast@v26.6.2` configura diretamente os endpoints de **produção** do XGuardian.

Ela não expõe `is_development` nesse contrato. Por isso o benchmark não apresenta mais seletor development/production no workflow.

## Execução manual

1. Configure `XGUARDIAN_TOKEN`, `XGUARDIAN_TEAM_ID` e `XGUARDIAN_LANGUAGES`.
2. Abra **Actions → XGuardian SAST Accuracy Benchmark**.
3. Clique em **Run workflow**.

## Execução automática

Defina:

```text
XGUARDIAN_PIPELINE_ENABLED=true
```

Com essa variável, mudanças relevantes em `cases/**`, no ground truth ou no workflow integradas em `main` podem disparar um novo scan.

Sem a variável, pushes não consomem scan.

## Resultado

A Action fornece:

- `app_id`;
- `scan_id`;
- `scan_url`;
- `scan_version`.

O workflow publica esses dados no **GitHub Job Summary**.

Após exportar o resultado SAST do XGuardian em JSON:

```bash
python3 benchmark_tools/evaluate_xguardian.py result.json --output-dir benchmark_score
```

## Rastreabilidade

Para cada execução relevante, registre junto ao score:

- commit do benchmark;
- `scan_id` e `scan_version`;
- SHA/tag da XGuardian Action;
- engine/scanners/rules observados;
- configuração de excludes e filtros;
- falhas parciais, se houver.

Não compare resultados de configurações diferentes como regressão ou evolução direta.
