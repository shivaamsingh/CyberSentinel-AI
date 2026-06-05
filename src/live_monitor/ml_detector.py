import joblib
from pathlib import Path
from feature_extractor import extract_features
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent.parent

model = joblib.load(
    BASE_DIR /
    "models" /
    "live_anomaly_detector.pkl"
)

def predict(flow):

    features = extract_features(flow)

    features = pd.DataFrame(
    [features],
    columns=[
        "Flow Duration",
        "Flow Bytes/s",
        "Flow Packets/s",
        "Average Packet Size"
    ]
)

    pred = model.predict(features)[0]

    if pred == -1:
        return "ANOMALY"

    return "NORMAL"