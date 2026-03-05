COLA – LEITURA E GRAVAÇÃO DE ARQUIVOS NO PROJETO 

Adicionar esta célula antes de qualquer import do projeto:

```python
import sys
from pathlib import Path

PROJECT_ROOT = Path.cwd().parents[2]
SRC_DIR = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_DIR))
```

Importar paths do projeto

```python
from ds_core.paths import (
    RAW_DATA_DIR,
    INTERIM_DATA_DIR,
    PROCESSED_DATA_DIR,
    EXTERNAL_DATA_DIR,
    NOTEBOOKS_DIR,
    OUTPUT_DIR,
)

import pandas as pd
```

---

LER ARQUIVO EM `data/raw/<curso>/<modulo>`

CSV

```python
df = pd.read_csv(
    RAW_DATA_DIR / "curso_1" / "estatistica_descritiva" / "arquivo.csv"
)
```

Excel

```python
df = pd.read_excel(
    RAW_DATA_DIR / "curso_1" / "estatistica_descritiva" / "arquivo.xlsx"
)
```

Parquet

```python
df = pd.read_parquet(
    RAW_DATA_DIR / "curso_1" / "estatistica_descritiva" / "arquivo.parquet"
)
```

---

SALVAR DATASET EM `data/interim/<curso>/<modulo>`

```python
out_path = INTERIM_DATA_DIR / "curso_1" / "estatistica_descritiva" / "dados_tratamento_inicial.csv"
out_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(out_path, index=False)
```

ou

```python
out_path = INTERIM_DATA_DIR / "curso_1" / "estatistica_descritiva" / "dados_tratamento_inicial.parquet"
out_path.parent.mkdir(parents=True, exist_ok=True)

df.to_parquet(out_path)
```

---

SALVAR DATASET EM `data/processed/<curso>/<modulo>`

```python
out_path = PROCESSED_DATA_DIR / "curso_1" / "estatistica_descritiva" / "dataset_final.csv"
out_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(out_path, index=False)
```

ou

```python
out_path = PROCESSED_DATA_DIR / "curso_1" / "estatistica_descritiva" / "dataset_final.parquet"
out_path.parent.mkdir(parents=True, exist_ok=True)

df.to_parquet(out_path)
```

---

SALVAR FIGURAS EM `outputs/figures/<curso>/<modulo>`

```python
import matplotlib.pyplot as plt

fig_path = OUTPUT_DIR / "figures" / "curso_1" / "estatistica_descritiva" / "distribuicao_preco.png"
fig_path.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(fig_path, dpi=300, bbox_inches="tight")
```

---

SALVAR RELATÓRIOS OU TABELAS EM `outputs/reports/<curso>/<modulo>`

```python
report_path = OUTPUT_DIR / "reports" / "curso_1" / "estatistica_descritiva" / "estatisticas_descritivas.csv"
report_path.parent.mkdir(parents=True, exist_ok=True)

df.describe().to_csv(report_path)
```

ou

```python
report_path = OUTPUT_DIR / "reports" / "curso_1" / "estatistica_descritiva" / "analise_final.xlsx"
report_path.parent.mkdir(parents=True, exist_ok=True)

df_resultado.to_excel(report_path, index=False)
```

---

CRIAR PASTAS AUTOMATICAMENTE (caso não existam)

```python
(PROCESSED_DATA_DIR / "curso_1" / "estatistica_descritiva").mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "figures" / "curso_1" / "estatistica_descritiva").mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "reports" / "curso_1" / "estatistica_descritiva").mkdir(parents=True, exist_ok=True)
```

---

FLUXO MAIS COMUM NO DIA A DIA

1. ler dataset

```python
df = pd.read_csv(
    RAW_DATA_DIR / "curso_1" / "estatistica_descritiva" / "dataset.csv"
)
```

2. limpar / transformar

3. salvar dataset intermediário

```python
out_path = INTERIM_DATA_DIR / "curso_1" / "estatistica_descritiva" / "dataset_limpo.parquet"
out_path.parent.mkdir(parents=True, exist_ok=True)

df.to_parquet(out_path)
```

4. salvar dataset final

```python
out_path = PROCESSED_DATA_DIR / "curso_1" / "estatistica_descritiva" / "dataset_final.parquet"
out_path.parent.mkdir(parents=True, exist_ok=True)

df.to_parquet(out_path)
```

5. salvar gráficos

```python
fig_path = OUTPUT_DIR / "figures" / "curso_1" / "estatistica_descritiva" / "grafico.png"
fig_path.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(fig_path, dpi=300, bbox_inches="tight")
```

---

REGRA RÁPIDA PARA LEMBRAR

data/raw/<curso>/<modulo>
dados originais

data/interim/<curso>/<modulo>
dados em transformação

data/processed/<curso>/<modulo>
dados prontos

outputs/figures/<curso>/<modulo>
gráficos

outputs/reports/<curso>/<modulo>
tabelas e resultados finais
