import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = ROOT / "data" / "raw" / "store_dataset.csv"
OUT_DIR = ROOT / "data" / "processed"
OUT_FILE = OUT_DIR / "model_ready.csv"

REQUIRED_COLUMNS = [
    "store_id", "label", "url", "https", "contact_clarity",
    "refund_policy", "delivery_policy", "discount_anomaly",
    "review_uniformity", "social_activity", "domain_age_days"
]

def normalise_label(value):
    value = str(value).strip().lower()
    if value in {"fake", "fraud", "scam"}:
        return "fake"
    if value in {"legitimate", "real", "genuine"}:
        return "legitimate"
    return None

def preprocess_data():
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {RAW_FILE}")

    df = pd.read_csv(RAW_FILE)
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df["label"] = df["label"].map(normalise_label)
    df = df.dropna(subset=["label"])
    df["url_normalised"] = (
        df["url"].astype(str).str.strip().str.lower().str.rstrip("/")
    )
    df = df.drop_duplicates(subset=["store_id", "url_normalised"])

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_FILE, index=False)

    print(f"Processed records: {len(df)}")
    print(df["label"].value_counts())
    print(f"Saved to: {OUT_FILE}")

if __name__ == "__main__":
    preprocess_data()
