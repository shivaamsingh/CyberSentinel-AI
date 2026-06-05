import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_csv(
    r"C:\Projects\CyberSentinel-AI\data\processed\multiclass_balanced.csv"
)

X = df[
[
    "Flow Duration",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Average Packet Size"
]
]

model = IsolationForest(
    contamination=0.05,
    random_state=42
)

model.fit(X)

joblib.dump(
    model,
    "models/live_anomaly_detector.pkl"
)

print("Model saved")