# Metodologia

## Objetivo

Medir a eficácia de detecção e, principalmente, a capacidade de **discriminar código vulnerável de código semelhante porém seguro** no pipeline SAST efetivo do XGuardian.

## Princípios

1. Uma condição pontuada por arquivo.
2. Ground truth explícito com ID, linguagem, caminho, linhas, CWE, categoria, variante e racional.
3. Pares positivo/negativo sempre que viável.
4. Hard-negatives com APIs/sinks semelhantes, porém uso seguro.
5. Honeypots para expor regras puramente lexicais.
6. Dificuldade crescente: basic, medium, advanced, interprocedural e honeypot.
7. Independência de rule-id proprietário.
8. Taxonomia/CWE medida separadamente da detecção.
9. Nenhum segredo real.
10. Nenhum trecho vulnerável precisa ser executado em runtime.

## Unidade de pontuação

A unidade é **caso**, não o número bruto de findings:

- vulnerável + detectado = TP
- vulnerável + não detectado = FN
- benigno + não detectado = TN
- benigno + detectado = FP

O matcher usa caminho + intervalo de linhas com tolerância configurável. Em arquivo benigno, qualquer finding conta como FP. Em arquivo positivo, findings fora da região anotada são preservados como `extraneous` para auditoria.

## Métricas

Precision, Recall/TPR, FPR, Specificity, F1, Accuracy, Balanced Accuracy, MCC, score OWASP-style (`100 × (TPR − FPR)`) e Taxonomy Accuracy.

## Tracks

- `core`: C, C++, C#, Go, Java, JavaScript, PHP, Python, Ruby e TypeScript.
- `iac`: Terraform.

A separação evita que a acurácia de IaC distorça a leitura do SAST de código tradicional.

## Limitações

Benchmark sintético não reproduz toda a complexidade de aplicações reais. Acurácia é propriedade de **versão + regras + configuração + escopo + pós-processamento**, não um número permanente do produto.
