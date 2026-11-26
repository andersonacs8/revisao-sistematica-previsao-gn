# Protocolo da revisão estruturada da literatura

**Versão:** 1.4 (18/11/2026) · **Status:** strings congeladas (v1.0); identificação concluída em 04/11/2026; extração concluída em 18/11/2026 (207 textos completos)
**Revisor:** autor (revisor único: triagem, extração e reavaliação cega de amostra; ver seções 6 e 10)
**Diretriz:** PRISMA 2020 (Page et al., 2021), nos itens aplicáveis a uma revisão estruturada (seção 11).

Qualquer mudança neste protocolo depois do início das buscas é registrada na seção 10 (desvios), com data e motivo.

---

## 1. Contexto e objetivo

A base de consumo diário de gás natural de 44 instalações industriais (ERP + SCADA, 2018–2026) permite estudar
a previsão de demanda no nível do consumidor. Esta revisão mapeia (i) como a demanda de gás natural tem sido
prevista nesse nível e (ii) o que se sabe sobre modelos locais, globais e de fundação em séries temporais de energia,
para identificar lacunas que a base pode responder.

**Recorte a partir da v1.4.** A revisão passa a ser um artigo próprio (artigo 1), com uma pergunta principal (seção 2).
Os estudos experimentais derivados das lacunas (por exemplo, um benchmark comum dos candidatos ao estado da arte em
bases industriais e públicas) são trabalhos separados e não fazem parte deste protocolo, exceto pela justificativa de
seleção de modelos, que sai da síntese (seção 8.4).

**Escopo das conclusões.** O bloco A (gás natural) é a busca sistemática e sustenta as conclusões do artigo 1.
O bloco B é uma busca dirigida a modelos locais, globais e de fundação em energia; não cobre a literatura geral de
previsão de carga elétrica e entra como evidência complementar sobre esses paradigmas, sem generalização para "energia".

## 2. Perguntas da revisão

**Pergunta principal (artigo 1, bloco A):** existe, na literatura de previsão de demanda de gás natural, uma família de
métodos (estatístico, ML clássico, rede neural, híbrido ou de fundação) que geralmente apresenta melhor desempenho, e o
desenho experimental dos estudos permite sustentar essa conclusão?

Perguntas descritivas (respondidas pelo fichamento, seção 7):

| Código | Pergunta | Bloco |
|---|---|---|
| Q1 | Que dados e tipos de série são usados (unidade prevista, consumidor, granularidade, horizonte, extensão, covariáveis, origem)? | A (B complementar) |
| Q2 | Que soluções são propostas (família, modelo, decomposição, metaheurística, local × global × fundação)? | A e B |
| Q3 | Como esses aspectos evoluem ao longo do tempo? | A |
| Q4 | Há agrupamentos ou associações entre características dos dados, do método e dos resultados? | A |
| Q5 | Que tabelas e gráficos resumem o mapeamento? | A e B |
| Q6 | Existe métrica comum que permita comparar os estudos? | A |
| Q7 | Qual modelo ou família vence dentro de cada estudo, e por quanto (ganho sobre o melhor concorrente)? | A |
| Q8 | Os estudos relatam simplicidade e custo computacional? | A e B |
| Q9 | Os estudos declaram a finalidade da previsão e um erro aceitável para ela? | A e B |

Perguntas analíticas (definidas antes da síntese; critérios na seção 8):

| Código | Pergunta |
|---|---|
| P1 | Consenso: alguma família vence com frequência e margem consistentes, sobretudo nos estudos de comparação neutros? |
| P2 | Comparabilidade: as diferenças de bases, métricas, granularidades, baselines e protocolos impedem a comparação direta entre estudos? |
| P3 | Viés do modelo proposto: o padrão de vitória do modelo proposto é compatível com viés de seleção de concorrentes, de ajuste, de métrica ou de publicação? |
| P4 | Candidatos ao estado da arte: com critério explícito, quais modelos devem compor um benchmark comum? |
| P5 | Lacunas e recomendações: o que a literatura ainda não responde, que experimento ajudaria a conciliar os resultados e que práticas, já consolidadas em outros campos, tornariam os estudos comparáveis? |

As perguntas Q1–Q4 da v1.3 estão contidas nas atuais: a antiga Q1 corresponde a Q1/Q2 (bloco A); as antigas Q2 e Q3
(local × global e fundação) correspondem a Q2 (bloco B); a antiga Q4 (qualidade dos dados, partida a frio) é tratada
nas observações do fichamento e em P5.

## 3. Fontes de informação

| Fonte | Papel | Acesso |
|---|---|---|
| Scopus | Banco principal | Portal de Periódicos CAPES (UFMG) |
| Web of Science Core Collection | Banco principal | Portal de Periódicos CAPES (UFMG) |
| arXiv | Literatura cinzenta, só bloco B (modelos de fundação são majoritariamente pré-prints) | Aberto |
| Snowballing | Referências (para trás) e citações (para frente, via Scopus/Google Scholar) dos artigos-semente | — |

IEEE Xplore fica como fonte opcional: só será usada se a calibração mostrar artigos relevantes ausentes de Scopus/WoS.

## 4. Estratégia de busca

### 4.1 Parâmetros comuns

- Campo: título, resumo e palavras-chave.
- Idioma: inglês (português aceito se aparecer).
- Tipos: artigo de periódico, artigo de congresso, revisão.
- Período: bloco A de 2015 a 2026; bloco B de 2018 a 2026.
- Data da busca: registrada na seção 9 e no nome do arquivo exportado.
- Exportação: Scopus em CSV com todos os campos (inclusive resumo); WoS em "Tab delimited file" com "Full record";
  arXiv em RIS (ou BibTeX convertido para RIS).

### 4.2 Bloco A: previsão de demanda de gás natural (Q1, Q4)

**Scopus**
```
TITLE-ABS-KEY ( ( "natural gas" OR "gas distribution" OR "city gate*" OR "gas network*" )
  AND ( demand OR consumption OR load OR sendout )
  AND ( forecast* OR predict* )
  AND ( industr* OR customer* OR consumer* OR "end-use*" OR daily OR "short-term" OR "day-ahead" ) )
AND PUBYEAR > 2014 AND PUBYEAR < 2027
AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "cp" ) OR LIMIT-TO ( DOCTYPE , "re" ) )
AND ( LIMIT-TO ( LANGUAGE , "English" ) OR LIMIT-TO ( LANGUAGE , "Portuguese" ) )
```

**Web of Science**
```
TS=( ("natural gas" OR "gas distribution" OR "city gate*" OR "gas network*")
  AND (demand OR consumption OR load OR sendout)
  AND (forecast* OR predict*)
  AND (industr* OR customer* OR consumer* OR "end-use*" OR daily OR "short-term" OR "day-ahead") )
AND PY=(2015-2026)
AND DT=(Article OR Proceedings Paper OR Review)
```

### 4.3 Bloco B: modelos locais, globais e de fundação em energia (Q2, Q3)

**Scopus**
```
TITLE-ABS-KEY ( ( "global model*" OR "global forecasting model*" OR "local model*" OR "cross-learning"
    OR "pooled model*" OR "foundation model*" OR "pre-trained model*" OR "pretrained model*"
    OR "zero-shot" OR "large time series model*" )
  AND ( "time series" ) AND ( forecast* )
  AND ( energy OR electricity OR "natural gas" OR load OR demand ) )
AND PUBYEAR > 2017 AND PUBYEAR < 2027
AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "cp" ) OR LIMIT-TO ( DOCTYPE , "re" ) )
```

**Web of Science**
```
TS=( ("global model*" OR "global forecasting model*" OR "local model*" OR "cross-learning" OR "pooled model*"
    OR "foundation model*" OR "pre-trained model*" OR "pretrained model*" OR "zero-shot" OR "large time series model*")
  AND "time series" AND forecast*
  AND (energy OR electricity OR "natural gas" OR load OR demand) )
AND PY=(2018-2026)
AND DT=(Article OR Proceedings Paper OR Review)
```

**arXiv** (busca avançada, campo *abstract*, 2023–2026, categorias cs.LG, stat.ML, eess.SY):
```
"foundation model" AND "time series" AND (energy OR load OR electricity)
"zero-shot" AND "time series" AND forecasting AND (energy OR load)
```

### 4.4 Calibração (antes da busca definitiva)

1. Rodar as strings e anotar o número de resultados de cada iteração na seção 9.
2. Verificar se os **artigos de controle** (4.5) são recuperados. Se algum não aparecer, ajustar a string e registrar a mudança.
3. Alvo indicativo: algumas centenas de registros por bloco. Se passar de ~1.000, restringir os termos de contexto
   (ex.: exigir `forecast*` no título) em vez de usar NOT.
4. Congelar as strings (versão 1.0 → 1.1, se mudarem) e fazer a busca definitiva no mesmo dia em todas as bases.

### 4.5 Artigos de controle e sementes do snowballing

Artigos que as buscas **devem** recuperar (validação das strings) e que servem de semente ao snowballing.
Confirmar referências completas na calibração; completar o bloco A com 2 ou 3 artigos de previsão de gás já
conhecidos (ex.: os citados no manuscrito anterior).

| Bloco | Referência | Papel |
|---|---|---|
| A | Gaweł & Paliński (2024), *Energies* 17(2), 347: local × global em consumo de gás na Polônia | controle + semente |
| A | *(a completar pelo autor)* | controle |
| B | Montero-Manso & Hyndman (2021), *International Journal of Forecasting*: localidade e globalidade | semente (metodológico, fora do domínio de energia) |
| B | Hewamalage, Bergmeir & Bandara (2022), *Pattern Recognition*: estudo de simulação de modelos globais | semente (metodológico) |
| B | Ansari et al. (2024): Chronos | semente (modelo de fundação) |
| B | Das et al. (2024): TimesFM | semente (modelo de fundação) |
| B | FETS Benchmark (2026, arXiv 2604.22328): modelos de fundação em séries de energia | controle + semente |

Snowballing: uma rodada para trás e uma para frente sobre as sementes e sobre os incluídos mais relevantes
(registrados como `snowball_<bloco>_<data>.ris`). Os registros passam pela mesma triagem.

## 5. Critérios de elegibilidade

Os códigos são usados na coluna de motivo da triagem (`ta_motivo`, `tc_motivo`).

### Inclusão

| Código | Critério |
|---|---|
| IC1 | Estudo empírico que gera e avalia previsões fora da amostra (ou revisão sistemática sobre o tema). |
| IC2 | **Bloco A:** variável prevista é demanda/consumo de gás natural no nível de consumidor, grupo de consumidores, setor, city-gate, rede de distribuição, região ou país; no nível nacional, só com granularidade diária ou mensal (a anual cai em EC2). |
| IC3 | **Bloco B:** compara modelos locais e globais (inclusive transferência de aprendizado ou aprendizado federado entre séries), ou avalia modelos de fundação, em séries temporais de **demanda, consumo ou carga de energia** (eletricidade, gás, calor, edificações, recarga de veículos). Séries de geração (fotovoltaica, eólica) e de preço não entram. |
| IC4 | Reporta métricas de erro quantitativas. |

### Exclusão

| Código | Critério |
|---|---|
| EC1 | Previsão de preço, produção, reservas, importação/exportação ou comércio de GNL. **Usar só nesses casos**; outro alvo que não seja demanda de gás é EC4. |
| EC2 | Agregado **nacional** com granularidade anual (modelos econométricos, cinza ou de tendência); fica como referência de contexto, fora da extração. Séries anuais regionais ou municipais não caem aqui. |
| EC3 | Sem avaliação fora da amostra ou sem métricas. |
| EC4 | Fora do domínio (não é gás no bloco A; não é energia nem a comparação pedida no bloco B). |
| EC5 | Resumo expandido, editorial, tese/dissertação, capítulo de livro ou texto completo indisponível. |
| EC6 | Idioma diferente de inglês ou português. |
| EC7 | Duplicata ou versão anterior de estudo já incluído (fica a versão mais completa; pré-print substituído pelo publicado). |

## 6. Processo de seleção

1. **Consolidação:** `python -m base_gn.revisao consolidar` junta as exportações e remove duplicatas por DOI e, sem DOI, por título normalizado.
2. **Piloto de calibração:** o revisor tria 30 registros (15 de cada bloco, sorteio com semente fixa), confronta cada decisão
   com os critérios e, se a redação de algum critério se mostrar ambígua, ajusta-a antes da triagem completa (ajuste registrado na seção 10).
3. **Título e resumo:** o revisor tria todos os registros em `triagem.xlsx` (`ta_decisao`: I inclui, E exclui, T talvez; `ta_motivo` com o código EC).
   **Regra conservadora:** na dúvida, marca-se T, e o registro segue para o texto completo.
4. **Confiabilidade intraexaminador:** `python -m base_gn.revisao amostra` sorteia 10% dos registros (semente 2026, fora do piloto) para uma
   **reavaliação cega** (`triagem_reavaliacao.xlsx`), feita sem consultar a primeira triagem e pelo menos 14 dias depois dela.
   `python -m base_gn.revisao kappa` calcula o kappa de Cohen entre as duas avaliações. As divergências são revistas contra os critérios
   e a decisão final é registrada em `ta_obs`. Se o kappa for menor que 0,6, os critérios são reescritos e a triagem é refeita.
5. **Texto completo:** o revisor obtém o PDF (`tc_obtido` S/N) e avalia (`tc_decisao` I/E, `tc_motivo`). Casos que permanecerem duvidosos
   são listados e, quando possível, discutidos com o orientador; a decisão e o motivo ficam em `tc_obs`.
6. **Fluxograma:** `python -m base_gn.revisao prisma` gera as contagens e o fluxograma PRISMA 2020.

## 7. Extração de dados

**Formulário (v3, a partir de 13/11/2026).** A extração é feita em `fichamento.xlsx` (substitui `extracao.xlsx`), uma linha por
texto completo avaliado, com listas fechadas na aba `listas` e a pergunta (Q1–Q9) que cada coluna atende no cabeçalho.
Grupos de campos: identificação; dados (unidade prevista, tipo de consumidor, granularidade, horizonte, nº de séries,
extensão, clima, calendário, origem); método (família, modelo proposto, decomposição do sinal, metaheurística,
local/global/fundação); métricas (MAPE, RMSE, MAE, R², MASE, métrica principal); resultado (erro do proposto, erro do
melhor concorrente, ganho, classe do concorrente, comparação com ingênuo, validação, teste de significância); custo; finalidade e exigência declarada; achado principal, páginas-fonte e observações.
Um piloto de 5 estudos precedeu a versão final do formulário.

**Regras de codificação.**
- *Modelo proposto:* o modelo apresentado pelos autores; em estudos comparativos sem modelo próprio (benchmark), o melhor modelo do estudo.
- *Melhor concorrente:* o melhor modelo de família **diferente** da do proposto; se todos forem da mesma família, o segundo melhor.
- *Ganho sobre o melhor concorrente:* (erro do concorrente − erro do proposto) / erro do concorrente × 100, na métrica principal
  (menor é melhor); valores informados só no texto (ex.: "até 23,6%") são registrados à mão e assinalados nas observações.
- *Família:* modelos lineares (DLinear, regressões) e modelos cinza contam como estatísticos; cinza combinado com ML conta como híbrido.
- Estudos com apenas métricas intervalares, ou com erros só em gráficos, entram com os campos de erro em branco.
- Publicações redundantes (mesmo estudo em mais de um veículo) entram como **um** estudo na síntese.

**Colunas acrescentadas na v1.4 (só bloco A).**
- *Nº de concorrentes:* modelos externos comparados ao proposto, sem contar variantes e ablações do próprio proposto.
- *Ajuste dos concorrentes descrito?:* **Sim** (os concorrentes passam por busca de hiperparâmetros descrita, ou pelo mesmo
  procedimento do proposto); **parcial** (hiperparâmetros fixos informados, sem busca); **Não** (nada informado).
Essas colunas servem à P3 (seleção de concorrentes e ajuste desigual).

**Extração com apoio de IA e verificação.** A extração foi feita por IA (Claude, Anthropic) a partir dos PDFs, com indicação
das páginas-fonte de cada ficha, em lotes revisados pelo autor. A verificação é uma **reavaliação cega de 10%** dos
estudos incluídos (sorteio estratificado por bloco e ano, semente fixa): o autor preenche as colunas de extração sem ver
as respostas da primeira extração; mede-se a concordância (kappa de Cohen nas colunas categóricas; diferença absoluta
nos campos numéricos). Divergências são revistas contra o texto, e as regras de codificação são reescritas, com nova
conferência das colunas afetadas, se o kappa de alguma coluna-chave (família, classe do concorrente, ingênuo, validação)
for menor que 0,6.

## 8. Avaliação dos estudos e síntese

Não há ferramenta consagrada de risco de viés para estudos de previsão; usa-se uma lista de verificação de rigor
metodológico, derivada dos campos de extração: (a) dados descritos; (b) avaliação fora da amostra com origem móvel;
(c) referências ingênuas/estatísticas no comparativo; (d) métrica escalada ou adequada a zeros; (e) teste de significância;
(f) dados ou código disponíveis. Cada item vale 0/1; o escore é descritivo, não critério de exclusão.

Síntese narrativa, com tabelas de mapeamento de lacunas, por exemplo abordagem × tipo de consumidor × granularidade
e frequência de cada item de rigor ao longo dos anos.

### 8.0 Arco da análise (nota de 19/11/2026)

As análises e os resultados seguem três passos: (1) a literatura permite verificar consenso? (P2, comparabilidade);
(2) se não, o que mostra a melhor evidência disponível, o desempenho relativo dentro de cada estudo? (P1 e P3);
(3) o que tornaria a área comparável? (P4 e P5, com recomendações ligadas a cada deficiência medida).
A nota reordena a apresentação e acrescenta recomendações à P5; não cria análise nova.

### 8.1 Consenso entre famílias (P1)

- A unidade de análise é o estudo empírico do bloco A (revisões excluídas; publicações redundantes contadas uma vez).
- Os estudos são separados em **comparações neutras** (tipo "benchmark": os autores não propõem modelo próprio) e
  **estudos com modelo proposto**. As comparações neutras são a referência principal para julgar consenso, porque não têm
  modelo a defender.
- Para cada família: número de estudos em que vence, nos dois grupos; mediana e intervalo interquartil do ganho.
- Há **consenso** se uma família vence em pelo menos 2/3 das comparações neutras que a incluem e não perde de forma
  recorrente nos estudos com modelo proposto; **tendência** se vence na maioria simples; **ausência de consenso** nos demais casos.
- Com poucas comparações neutras, o resultado é descrito como indicativo.
- O mesmo critério é aplicado por período de publicação e de forma acumulada, para verificar se alguma família desponta ao longo do tempo (tabela P1b do notebook).

### 8.2 Comparabilidade (P2)

Frequências de: métrica principal, uso de MAPE e de métrica escalada, comparação com ingênuo/sazonal, validação,
granularidade e unidade prevista, origem dos dados. A falta de uma métrica e de um baseline comuns é tratada como resultado.

### 8.3 Indicadores de viés do modelo proposto (P3)

Indicadores definidos antes da análise; a revisão relata padrões **compatíveis** com viés, sem afirmar sua existência
(viés de publicação não é demonstrável só com estudos publicados):
1. proporção de estudos com modelo proposto em que o proposto vence;
2. ganho mediano nos estudos com modelo proposto × nas comparações neutras;
3. ganho segundo o nº de concorrentes, o ajuste dos concorrentes descrito, a comparação com ingênuo e o tipo de validação;
4. famílias que aparecem como proposto × como melhor concorrente.
Estratificação descritiva; sem metarregressão (poucos estudos e heterogeneidade alta).

### 8.4 Candidatos ao estado da arte e seleção para o benchmark (P4)

A revisão não declara "os melhores modelos"; lista **candidatos**, com critério explícito: (a) vencem ou ficam entre os
melhores nas comparações neutras; (b) aparecem como concorrente forte em vários estudos independentes; (c) representam as
famílias recentes (globais e de fundação, a partir do bloco B); (d) têm implementação aberta e madura.

Modelos híbridos propostos uma única vez (combinações específicas de decomposição do sinal, otimização metaheurística e
aprendiz) não entram na lista se: não forem replicados por grupos independentes; não tiverem código disponível; dependerem
de decomposição aplicada à série inteira (risco de vazamento); ou não vencerem comparações neutras. A justificativa é
apresentada com os indicadores das seções 8.1 e 8.3.

### 8.5 Lacunas e experimento conciliador (P5)

Lacunas tiradas das frequências do fichamento (ex.: consumidor industrial individual, baselines, métricas escaladas,
origem móvel, testes de significância, exigência declarada, partida a frio). O experimento proposto é derivado dessas
lacunas e descrito como consequência da síntese, não como hipótese prévia.

## 9. Registro das buscas

Preencher a cada execução (inclusive as de calibração). O arquivo exportado vai para `references/revisao/buscas/`
com o nome `<base>_<bloco>_<AAAAMMDD>.<ext>` e **nunca é editado**.

| Data | Base | Bloco | Versão da string | Filtros aplicados | Resultados | Arquivo exportado | Observação |
|---|---|---|---|---|---|---|---|
| 04/11/2026 | Scopus | A | 1.0 | 2015–2026; ar, cp, re; inglês/português | 1.234 | `scopus_A_20261104.csv` | definitiva |
| 04/11/2026 | WoS | A | 1.0 | 2015–2026; Article, Proceedings Paper, Review | 1.022 | `wos_A_20261104_part1.txt`, `_part2.txt` | definitiva (exportação em 2 partes: limite de 1.000) |
| 04/11/2026 | Scopus | B | 1.0 | 2018–2026; ar, cp, re | 325 | `scopus_B_20261104.csv` | definitiva |
| 04/11/2026 | WoS | B | 1.0 | 2018–2026; Article, Proceedings Paper, Review | 228 | `wos_B_20261104.txt` | definitiva |
| 04/11/2026 | arXiv (API) | B | 1.0 | 2023–2026; cs.LG, stat.ML, eess.SY; campo resumo | 80 + 36 (88 únicos) | `arxiv_B_20261104.ris` | consultas exatas em `registro_buscas_arxiv.md` |

Consolidação (04/11/2026): 2.897 registros brutos, 965 duplicatas, **1.932 registros únicos** (1.860 de bancos, 72 só do arXiv).
Artigos de controle: recuperados Gaweł & Paliński (2024) e FETS (2026); Montero-Manso & Hyndman, Hewamalage et al., Chronos e TimesFM
originais não recuperados, como esperado (fora do domínio de energia ou não indexados): entram pelo snowballing.
Teste de restrição por proximidade no bloco A (gás a até 3 palavras de demanda/consumo) reduziria o bloco de 1.512 para ~600
registros, mas perdia estudos relevantes; as strings foram mantidas sem alteração.

## 10. Desvios do protocolo

| Data | Seção | Mudança | Motivo |
|---|---|---|---|
| 04/11/2026 | 4.3 | Busca no arXiv feita pela API pública, e não pela interface web. Uma primeira tentativa na interface (consultas unidas, campo título, 13 resultados) foi descartada. | A interface web não exporta resultados; a API aplica as consultas do protocolo no campo resumo, com filtros de data e categoria. |
| 04/11/2026 | 3 | IEEE Xplore não utilizado. | Os artigos de controle recuperáveis foram encontrados em Scopus/WoS; a fonte era opcional. |
| 08/11/2026 | 5 | EC2 restrito ao agregado nacional (antes: nacional ou regional); IC3 explicita séries de demanda/consumo/carga, inclui transferência e aprendizado federado entre séries, e exclui geração e preço. Criada a categoria "referência metodológica": estudos global × local ou de heterogeneidade fora do domínio de energia, excluídos por EC4 mas citados no capítulo (fora da contagem PRISMA). | A redação anterior do EC2 excluiria um artigo de controle com séries anuais municipais (Gaweł & Paliński, 2024); a do IC3 não refletia a regra aplicada na triagem. |
| 08/11/2026 | 6 | Segunda conferência da triagem com apoio de IA: correção mecânica dos códigos de motivo (105 incluídos, 44 excluídos) e 79 sugestões marcadas em `revisar` para decisão do autor. | Consistência dos códigos para o fluxograma e aplicação uniforme dos critérios v1.3. |
| 07/11/2026 | 5 | IC2 passa a aceitar o nível nacional com granularidade diária ou mensal; EC2 cobre qualquer agregado anual; EC1 restrito a preço/produção/comércio. | Ambiguidade observada na primeira triagem (previsões nacionais mensais por ML e uso genérico do EC1). |
| 07/11/2026 | 6 | Primeira triagem revisada com apoio de IA (Claude): sugestões de exclusão/talvez para 79 registros mantidos e sinalização de 173 excluídos com possível falso negativo (coluna `revisar`). As sugestões foram conferidas e aceitas pelo autor; os 173 são reavaliados manualmente. | Validação da triagem inicial; o uso de ferramenta de IA é declarado como automação (PRISMA 2020, item 8). |
| 19/11/2026 | 8.1 | Critério de consenso aplicado também por período e de forma acumulada. | Leitura temporal de "tendência" pedida pelo autor; o critério não muda. |
| 19/11/2026 | 7, 8.3 | Alerta de qualidade removido do estudo (formulário, regras, verificação e indicadores de viés); a coluna permanece no fichamento só como registro histórico, sem uso na síntese. | O alerta não foi reavaliado às cegas e depende de julgamento; os indicadores objetivos (nº de concorrentes, ajuste descrito, ingênuo, validação) sustentam a P3 sem ele. |
| 19/11/2026 | 2, 8 | P5 passa a incluir recomendações de prática, ligadas às deficiências medidas; acrescentada a seção 8.0 (arco da análise em três passos). | Dar ao artigo uma contribuição prática derivada dos dados; nenhuma análise nova foi criada. |
| 18/11/2026 | 1, 2 | Revisão passa a ser artigo próprio, com pergunta principal sobre consenso entre famílias de métodos (bloco A) e perguntas analíticas P1–P5; perguntas descritivas Q1–Q9 substituem Q1–Q4 da v1.3 (correspondência na seção 2); bloco B fica como evidência complementar. | A pergunta de pesquisa anterior foi abandonada; o problema de pesquisa passou a sair da síntese. Critérios de análise registrados antes da síntese para evitar análise post hoc. |
| 18/11/2026 | 7 | Extração em `fichamento.xlsx` (formulário v3) com apoio de IA e páginas-fonte; regras de codificação explícitas (proposto, concorrente de outra família, ganho, alerta de qualidade); verificação por reavaliação cega de 10% da extração; colunas "nº de concorrentes" e "ajuste dos concorrentes descrito?" acrescentadas ao bloco A. | Volume de 207 textos completos com revisor único; as novas colunas são necessárias para a P3. |
| 18/11/2026 | 8 | Acrescentadas as seções 8.1–8.5 (consenso, comparabilidade, indicadores de viés, candidatos ao estado da arte, lacunas). | Definir os critérios de análise antes da síntese. |
| 25/11/2026 | 4.5 | Snowballing (uma rodada para trás e uma para frente) não realizado; não houve busca por citações nem consulta a especialistas. | Decisão do autor; declarado no artigo (seção 3.2) e no checklist PRISMA (item 6). |
| 25/11/2026 | 7 | Extração refeita manualmente pelo autor, sem apoio de IA; a ferramenta de IA ficou restrita à conferência da triagem (seção 6). Autores dos estudos não contatados. | Decisão do autor; substitui a extração com apoio de IA registrada em 18/11/2026. |
| 04/11/2026 | 6 | Revisor único. O segundo revisor (amostra de 20%) foi substituído por piloto de calibração, regra conservadora e reavaliação cega de 10% com kappa intraexaminador. | Indisponibilidade do orientador para a triagem. |

## 11. Aderência ao PRISMA 2020 e limitações declaradas

Itens atendidos: critérios de elegibilidade (item 5), fontes e datas (6), estratégia completa de busca (7),
processo de seleção com revisor único, regra conservadora e concordância intraexaminador (8), processo e itens de extração (9–10),
avaliação de rigor (11), métodos de síntese (13), fluxograma (16a) e motivos de exclusão no texto completo (16b).

Limitações a declarar no capítulo:
- protocolo não registrado previamente (PROSPERO/OSF); opcionalmente registrar no OSF antes da busca definitiva;
- triagem e extração por um único revisor; a confiabilidade é estimada por reavaliação cega de 10% (kappa intraexaminador),
  que mede a consistência do revisor, mas não substitui um segundo revisor independente;
- literatura cinzenta restrita ao arXiv e ao snowballing;
- uso de ferramentas de IA como apoio à triagem e à extração (declarado nas seções 7 e 10), com decisão final do autor
  e verificação da extração por reavaliação cega de 10%;
- comparação entre estudos limitada pela heterogeneidade de métricas e bases: o ganho sobre o melhor concorrente é
  medido dentro de cada estudo e não permite ranquear modelos entre estudos;
- os indicadores de viés mostram padrões compatíveis com viés, mas não o demonstram;
- o bloco B é uma busca dirigida, não uma revisão sistemática da previsão de carga elétrica;
- sem meta-análise (estudos heterogêneos em dados, métricas e horizontes).

## 12. Arquivos

| Caminho | Conteúdo | Git |
|---|---|---|
| `references/revisao/protocolo_revisao.md` | Este protocolo | sim |
| `references/revisao/buscas/` | Exportações brutas das bases | sim |
| `references/revisao/registros_consolidados.csv` | Todos os registros com a origem de cada um | sim |
| `references/revisao/triagem.xlsx` | Decisões de triagem do revisor 1 | sim |
| `references/revisao/triagem_reavaliacao.xlsx` | Amostra da reavaliação cega (10%) | sim |
| `references/revisao/registro_buscas_arxiv.md` | Consultas exatas enviadas à API do arXiv | sim |
| `references/revisao/fichamento.xlsx` | Formulário de extração (v3), com listas fechadas | sim |
| `references/revisao/fichamento_reavaliacao.xlsx` | Amostra da reavaliação cega da extração (10%) | sim |
| `references/revisao/prisma_contagens.md`, `prisma_fluxograma.png` | Fluxo PRISMA | sim |
| `references/revisao/pdfs/` | Textos completos | **não** (direitos autorais) |

Referência da diretriz: Page, M. J. et al. (2021). The PRISMA 2020 statement: an updated guideline for reporting
systematic reviews. *BMJ*, 372, n71.
