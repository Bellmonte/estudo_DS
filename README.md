# 📊 estudo_DS — Projeto de Estudos em Data Science

Este repositório contém um ambiente estruturado para estudos em **Data Science**, com foco em organização de projetos, reprodutibilidade e boas práticas usadas em projetos profissionais.

A estrutura separa **dados, notebooks, código reutilizável e resultados**, facilitando o desenvolvimento e a replicação do projeto em qualquer máquina.

---

# 📁 Estrutura do Projeto

```
estudo_DS
│
├─ configs/              # Arquivos de configuração do projeto
│
├─ data/
│   ├─ raw/              # Dados brutos (originais)
│   ├─ interim/          # Dados em transformação
│   ├─ processed/        # Dados prontos para análise/modelagem
│   └─ external/         # Dados externos auxiliares
│
├─ notebooks/            # Análises e experimentação
│
├─ outputs/
│   ├─ figures/          # Gráficos gerados
│   └─ reports/          # Relatórios e resultados finais
│
├─ src/
│   └─ ds_core/          # Pacote Python com código reutilizável
│       ├─ __init__.py
│       ├─ paths.py
│       ├─ data.py
│       └─ features.py
│
├─ requirements.txt      # Dependências do projeto
├─ pyproject.toml        # Configuração do pacote Python
└─ README.md             # Documentação do projeto
```

---

# 🧠 Organização do Projeto

Este projeto segue o padrão **src layout**, amplamente utilizado em projetos profissionais de Python e Data Science.

Principais conceitos:

| Pasta       | Função                                |
| ----------- | ------------------------------------- |
| `notebooks` | Análises exploratórias e experimentos |
| `src`       | Código reutilizável                   |
| `data`      | Armazenamento de datasets             |
| `outputs`   | Resultados gerados pelo projeto       |
| `configs`   | Configurações do projeto              |

---

# ⚙️ Como Executar o Projeto

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/estudo_DS.git
cd estudo_DS
```

---

## 2️⃣ Criar ambiente virtual

```bash
python -m venv .venv
```

---

## 3️⃣ Ativar o ambiente

### Windows

```bash
.venv\Scripts\activate
```

### Mac / Linux

```bash
source .venv/bin/activate
```

---

## 4️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Instalar o pacote do projeto

```bash
pip install -e .
```

Esse comando registra o pacote `ds_core` no ambiente Python, permitindo imports como:

```python
from ds_core.paths import RAW_DATA_DIR
```

---

# 📦 Gerenciamento de Dados

Datasets **não são versionados no Git**.

Para utilizar o projeto:

1. Baixe os datasets necessários
2. Coloque os arquivos em:

```
data/raw/
```

A partir daí, os notebooks e scripts utilizam os caminhos centralizados definidos em:

```
src/ds_core/paths.py
```

---

# 🧩 Uso do `paths.py`

O arquivo `paths.py` centraliza os caminhos do projeto para evitar problemas de diretório.

Exemplo de uso:

```python
from ds_core.paths import RAW_DATA_DIR

import pandas as pd

df = pd.read_csv(RAW_DATA_DIR / "dataset.csv")
```

Isso permite que o projeto funcione independentemente da máquina onde está sendo executado.

---

# 📓 Organização dos Notebooks

Os notebooks seguem uma ordem lógica de desenvolvimento.

Exemplo:

```
01_exploracao.ipynb
02_limpeza_dados.ipynb
03_feature_engineering.ipynb
04_modelagem.ipynb
05_avaliacao_modelo.ipynb
```

Regras:

* notebooks contêm **análise e experimentação**
* código reutilizável deve ficar em `src`

---

# 🔁 Fluxo de Trabalho

Fluxo recomendado para desenvolvimento:

1. Colocar dataset em `data/raw`
2. Explorar dados em `notebooks`
3. Criar funções reutilizáveis em `src/ds_core`
4. Gerar outputs em `outputs`
5. Versionar código no GitHub

---

# 🚀 Replicando o Projeto em Outra Máquina

Para executar o projeto em outro computador:

```bash
git clone ...
cd estudo_DS

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
pip install -e .
```

Depois basta abrir os notebooks normalmente.

---

# 📚 Tecnologias Utilizadas

Principais ferramentas do projeto:

* Python
* Pandas
* NumPy
* Scikit-Learn
* Jupyter Notebook
* Git
* VS Code

---

# 🧑‍💻 Autor

Projeto desenvolvido para estudos e organização de projetos de Data Science.

---

# 📄 Licença

Uso educacional.
