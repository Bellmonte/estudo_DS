from pathlib import Path

# raiz do projeto
ROOT_DIR = Path(__file__).resolve().parents[2]

# diretórios principais
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

NOTEBOOKS_DIR = ROOT_DIR / "notebooks"
OUTPUT_DIR = ROOT_DIR / "outputs"