from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.api.threat_intel import router as threat_router
from src.api.copilot import router as copilot_router
from pathlib import Path
import joblib
import numpy as np
from src.api.report_generator import router as report_router
from src.api.rag_chat import router as rag_router
from src.api.investigator import router as investigator_router


app = FastAPI(
    title="CyberSentinel-AI",
    version="1.4"
)
app.include_router(
    threat_router
)
app.include_router(
    copilot_router
)
app.include_router(
    report_router
)
app.include_router(
    rag_router
)
app.include_router(
    investigator_router
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Load Models

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODELS_DIR = BASE_DIR / "models"

multiclass_model = joblib.load(
    MODELS_DIR / "multiclass_xgb_v1.pkl"
)

attack_encoder = joblib.load(
    MODELS_DIR / "attack_encoder.pkl"
)

iso_model = joblib.load(
    MODELS_DIR / "isolation_forest_v1.pkl"
)

scaler = joblib.load(
    MODELS_DIR / "anomaly_scaler.pkl"
)


# Input Schema

class TrafficData(BaseModel):
    features: list[float]


# Route


@app.get("/")
def home():
    return {
        "message": "CyberSentinel-AI Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
    
@app.post("/predict")
def predict(data: TrafficData):

    features = np.array(
        data.features
    ).reshape(1, -1)

    # Anomaly Detection
    

    scaled_features = scaler.transform(
        features
    )

    anomaly_pred = iso_model.predict(
        scaled_features
    )[0]

    anomaly = (
        True
        if anomaly_pred == -1
        else False
    )

    
    # Attack Detection


    attack_pred = multiclass_model.predict(
    features
    )[0]

    probs = multiclass_model.predict_proba(
    features
    )[0]

    confidence = float(
    np.max(probs)
    )

    attack_type = attack_encoder.inverse_transform(
        [attack_pred]
    )[0]

    
    # Risk Score
    

    risk = "LOW"

    if attack_type in [
    "PortScan",
    "BruteForce"
    ]:
        risk = "MEDIUM"

    if attack_type in [
    "DDoS",
    "DoS",
    "Bot",
    "WebAttack"
    ]:
     risk = "HIGH"

    if anomaly:
        risk = "CRITICAL"
    return {
    "attack_type": attack_type,
    "confidence": round(
        confidence,
        4
    ),
    "anomaly": anomaly,
    "risk_level": risk
}