from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = ROOT / "data" / "raw" / "store_dataset.csv"
PROCESSED_FILE = ROOT / "data" / "processed" / "model_ready.csv"
TARGET = "label"
RANDOM_STATE = 42
