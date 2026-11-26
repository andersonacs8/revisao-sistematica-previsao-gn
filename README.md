# Existe um método superior para prever a demanda de gás natural? Consenso e comparabilidade em uma revisão sistemática

Dados, código e materiais da revisão sistemática que avalia se há consenso, ou tendência de consenso, de que uma família de métodos apresenta desempenho geralmente superior na previsão de demanda de gás natural, e se o desenho experimental dos estudos permite sustentar essa conclusão. A revisão segue as diretrizes PRISMA 2020.

## Conteúdo

| Pasta | Arquivo | O que é |
|---|---|---|
| `protocolo/` | `protocolo_revisao.md` | Protocolo da revisão (versão 1.4), com perguntas, fontes, strings de busca, critérios, regras de codificação, plano de análise e registro datado de todos os desvios |
| `dados/` | `triagem.xlsx` | Os 1.932 registros únicos triados por título e resumo, com a decisão (I, E ou T) e os critérios aplicados |
| `dados/` | `fichamento.xlsx` | Base de dados extraídos dos 207 textos completos avaliados (aba `fichamento`), com as listas de valores (aba `listas`) e as perguntas de síntese (aba `guia`) |
| `notebooks/` | `sintese_revisao.ipynb` | Código que gera, a partir de `dados/fichamento.xlsx`, todas as tabelas e as figuras 4.2 e 4.5 do artigo |
| `figuras/` | `prisma.py`, `figs_resultados.py` | Scripts do fluxograma PRISMA (Figura 4.1) e das figuras 4.3, 4.4 e 4.6, com as imagens geradas |
| `suplementar/` | `material_suplementar.xlsx` | Material suplementar do artigo (estudos incluídos com características, indicadores de rigor e resultados, excluídos no texto completo e textos não obtidos) |

## Como reproduzir

**No Google Colab.** Abra `notebooks/sintese_revisao.ipynb` no Colab e execute todas as células. A primeira célula clona este repositório.

**Localmente.** Com Python 3.10 ou mais recente, instale `pandas`, `numpy`, `matplotlib`, `scipy` e `openpyxl` e execute o notebook a partir da pasta `notebooks/`. Os resultados são gravados em `resultados/` (tabelas em `sintese_tabelas.xlsx` e figuras em PNG). Os scripts da pasta `figuras/` rodam com `python prisma.py` e `python figs_resultados.py`.

Os valores das figuras 4.1, 4.3, 4.4 e 4.6 estão escritos nos scripts da pasta `figuras/` e foram transcritos das tabelas produzidas pelo notebook.

## Observações sobre os dados

- Os identificadores `R…` são internos e ligam a triagem, a base de dados extraídos e o material suplementar.
- Publicações redundantes (o mesmo estudo em mais de um veículo) aparecem na base, mas contam como um único estudo na síntese. O notebook as identifica no dicionário `REDUNDANTES`.
- Foram retiradas da base publicada as colunas de notas de trabalho do revisor (observações livres, achado principal, alerta de qualidade abandonado no protocolo, conferência e caminho do arquivo PDF). Nenhuma delas é usada nas análises.
- Os resumos dos registros e os textos completos dos estudos não são redistribuídos, por restrições de direitos autorais. Cada registro traz o DOI, quando disponível.

## Licença

Código (`notebooks/` e `figuras/*.py`): licença MIT, ver `LICENSE`. Dados, protocolo e material suplementar: CC BY 4.0, ver `LICENSE-DADOS.md`.

## Como citar

Ver `CITATION.cff`. O DOI do Zenodo será incluído aqui após a publicação da primeira versão.
