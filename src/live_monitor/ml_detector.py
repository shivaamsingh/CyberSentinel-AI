from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODELS_DIR = BASE_DIR / "models"

model = joblib.load(
    MODELS_DIR / "multiclass_xgb_v1.pkl"
)

encoder = joblib.load(
    MODELS_DIR / "attack_encoder.pkl"
)