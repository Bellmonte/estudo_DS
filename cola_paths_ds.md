COLINHA – LEITURA E GRAVAÇÃO DE ARQUIVOS NO PROJETO

Importar paths do projeto

```python
from ds_core.paths import (
    RAW_DATA_DIR,
    INTERIM_DATA_DIR,
    PROCESSED_DATA_DIR,
    EXTERNAL_DATA_DIR,
    FIGURES_DIR,
    REPORTS_DIR
)

import pandas as pd
```

---

LER ARQUIVO EM `data/raw`

CSV

```python
df = pd.read_csv(RAW_DATA_DIR / "arquivo.csv")
```

CSV dentro de pasta

```python
df = pd.read_csv(RAW_DATA_DIR / "estatistica_descritiva" / "ifood.csv")
```

Excel

```python
df = pd.read_excel(RAW_DATA_DIR / "arquivo.xlsx")
```

Parquet

```python
df = pd.read_parquet(RAW_DATA_DIR / "arquivo.parquet")
```

---

SALVAR DATASET EM `data/interim`

Usado para dados parcialmente tratados.

```python
df.to_csv(INTERIM_DATA_DIR / "dados_tratamento_inicial.csv", index=False)
```

ou

```python
df.to_parquet(INTERIM_DATA_DIR / "dados_tratamento_inicial.parquet")
```

---

SALVAR DATASET EM `data/processed`

Usado para dados prontos para análise ou modelagem.

```python
df.to_csv(PROCESSED_DATA_DIR / "dataset_final.csv", index=False)
```

ou

```python
df.to_parquet(PROCESSED_DATA_DIR / "dataset_final.parquet")
```

---

SALVAR FIGURAS EM `outputs/figures`

```python
import matplotlib.pyplot as plt

plt.savefig(FIGURES_DIR / "distribuicao_preco.png", dpi=300, bbox_inches="tight")
```

---

SALVAR RELATÓRIOS OU TABELAS EM `outputs/reports`

```python
df.describe().to_csv(REPORTS_DIR / "estatisticas_descritivas.csv")
```

ou

```python
df_resultado.to_excel(REPORTS_DIR / "analise_final.xlsx", index=False)
```

---

CRIAR PASTAS AUTOMATICAMENTE (caso não existam)

```python
(PROCESSED_DATA_DIR).mkdir(parents=True, exist_ok=True)
```

exemplo completo

```python
output_path = PROCESSED_DATA_DIR / "dataset_final.csv"

output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path, index=False)
```

---

FLUXO MAIS COMUM NO DIA A DIA

1. ler dataset

```python
df = pd.read_csv(RAW_DATA_DIR / "dataset.csv")
```

2. limpar / transformar

3. salvar dataset intermediário

```python
df.to_parquet(INTERIM_DATA_DIR / "dataset_limpo.parquet")
```

4. salvar dataset final

```python
df.to_parquet(PROCESSED_DATA_DIR / "dataset_final.parquet")
```

5. salvar gráficos

```python
plt.savefig(FIGURES_DIR / "grafico.png")
```

---

REGRA RÁPIDA PARA LEMBRAR

raw
dados originais

interim
dados em transformação

processed
dados prontos

outputs/figures
gráficos

outputs/reports
tabelas e resultados finais
