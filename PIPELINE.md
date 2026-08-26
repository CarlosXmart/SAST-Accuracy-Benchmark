# Pipeline XGuardian SAST

## Objetivo

Executar exclusivamente o corpus controlado em `cases/` pelo fluxo oficial do XGuardian usando a Action SAST publicada em `xguardian-actions/actions`.

## Referência oficial

A pipeline usa:

```text
xguardian-actions/actions/sast@6373d9375d3a859f602dcf53b37a3d8326c8a248
```

Esse SHA corresponde à release `v26.6.2` e evita alteração silenciosa do comportamento histórico do benchmark.

## `languages` é necessário?

Não para a execução do SAST deste benchmark.

Na Action SAST atual, `languages` é um input opcional ligado ao fluxo de identificação/criação da aplicação. O scanner recebe o código-fonte e o XGuardian faz sua própria detecção de linguagens no fluxo de análise.

Para evitar metadata incorreta — por exemplo, a Action aplicar o default `["JavaScript"]` em um benchmark poliglota — este workflow usa uma aplicação de benchmark já existente por `app_id`. Assim não são necessários `app_name`, `team_id` nem `languages` na execução.

## Configuração obrigatória

Em **Settings → Secrets and variables → Actions** configure:

### Repository Secret

- `XGUARDIAN_TOKEN` — PAT válido gerado na plataforma XGuardian.

### Repository Variable

- `XGUARDIAN_APP_ID` — ID numérico positivo da aplicação dedicada ao benchmark.
- `XGUARDIAN_PIPELINE_ENABLED` — opcional; use `true` somente se quiser scan automático em pushes relevantes de `main`.

A aplicação indicada por `XGUARDIAN_APP_ID` deve pertencer à organização correta e estar autorizada para o uso pretendido. O workflow não cria aplicações automaticamente.

## O que entra no scan

Somente:

```text
cases/
```

A Action recebe:

```yaml
scan_directory: "cases"
```

Portanto `README.md`, `PIPELINE.md`, `.github/`, `benchmark_meta/`, `benchmark_tools/` e qualquer outro caminho fora de `cases/` não são empacotados para o scan.

Antes de chamar a Action, o workflow remove apenas do workspace temporário:

```text
cases/typescript/tsconfig.json
```

Esse arquivo existe para validação local de TypeScript, mas não é um dos 164 casos pontuados. A remoção não altera o repositório; afeta apenas o checkout efêmero do runner.

O `cases/go/go.mod` permanece dentro do payload porque fornece contexto de módulo para o track Go e não é um caso de vulnerabilidade pontuado.

Com isso, a massa efetiva do SAST fica equivalente ao payload controlado do benchmark: os 164 casos de source code mais o `go.mod` auxiliar.

## Configuração do scan

```text
app_id: XGUARDIAN_APP_ID
scan_directory: "cases"
translate: "false"
pdf: "false"
get_scan_id: "true"
```

Não há necessidade de `exclude` para remover o restante do repositório, porque esses arquivos já ficam fora do diretório empacotado.

## Ambiente

A Action específica `xguardian-actions/actions/sast@v26.6.2` configura diretamente endpoints de produção do XGuardian. Ela não expõe `is_development` nesse contrato.

## Execução manual

1. Configure `XGUARDIAN_TOKEN` e `XGUARDIAN_APP_ID`.
2. Abra **Actions → XGuardian SAST Accuracy Benchmark**.
3. Clique em **Run workflow**.

## Execução automática

Defina:

```text
XGUARDIAN_PIPELINE_ENABLED=true
```

Sem essa variável, pushes em `main` não consomem scan.

## Resultado

A Action fornece `app_id`, `scan_id`, `scan_url` e `scan_version`. O workflow publica esses dados no **GitHub Job Summary**.

Após exportar o resultado SAST do XGuardian em JSON:

```bash
python3 benchmark_tools/evaluate_xguardian.py result.json --output-dir benchmark_score
```

## Rastreabilidade

Para cada execução relevante, registre:

- commit do benchmark;
- `scan_id` e `scan_version`;
- `XGUARDIAN_APP_ID` utilizado;
- SHA/tag da XGuardian Action;
- engine/scanners/rules observados;
- falhas parciais ou diferenças de configuração.

Não compare resultados de configurações diferentes como regressão ou evolução direta.
