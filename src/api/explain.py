from fastapi import APIRouter
from pydantic import BaseModel
from pathlib import Path

import joblib
import numpy as np
import shap


router = APIRouter()


BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODELS_DIR = BASE_DIR / "models"


model = joblib.load(
    MODELS_DIR / "multiclass_xgb_v1.pkl"
)

encoder = joblib.load(
    MODELS_DIR / "attack_encoder.pkl"
)


feature_names = [
    "Destination Port",
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Total Length of Fwd Packets",
    "Total Length of Bwd Packets",
    "Fwd Packet Length Max",
    "Fwd Packet Length Min",
    "Fwd Packet Length Mean",
    "Fwd Packet Length Std",
    "Bwd Packet Length Max",
    "Bwd Packet Length Min",
    "Bwd Packet Length Mean",
    "Bwd Packet Length Std",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Flow IAT Mean",
    "Flow IAT Std",
    "Flow IAT Max",
    "Flow IAT Min",
    "Fwd IAT Total",
    "Fwd IAT Mean",
    "Fwd IAT Std",
    "Fwd IAT Max",
    "Fwd IAT Min",
    "Bwd IAT Total",
    "Bwd IAT Mean",
    "Bwd IAT Std",
    "Bwd IAT Max",
    "Bwd IAT Min",
    "Fwd PSH Flags",
    "Bwd PSH Flags",
    "Fwd URG Flags",
    "Bwd URG Flags",
    "Fwd Header Length",
    "Bwd Header Length",
    "Fwd Packets/s",
    "Bwd Packets/s",
    "Min Packet Length",
    "Max Packet Length",
    "Packet Length Mean",
    "Packet Length Std",
    "Packet Length Variance",
    "FIN Flag Count",
    "SYN Flag Count",
    "RST Flag Count",
    "PSH Flag Count",
    "ACK Flag Count",
    "URG Flag Count",
    "CWE Flag Count",
    "ECE Flag Count",
    "Down/Up Ratio",
    "Average Packet Size",
    "Avg Fwd Segment Size",
    "Avg Bwd Segment Size",
    "Fwd Header Length.1",
    "Fwd Avg Bytes/Bulk",
    "Fwd Avg Packets/Bulk",
    "Fwd Avg Bulk Rate",
    "Bwd Avg Bytes/Bulk",
    "Bwd Avg Packets/Bulk",
    "Bwd Avg Bulk Rate",
    "Subflow Fwd Packets",
    "Subflow Fwd Bytes",
    "Subflow Bwd Packets",
    "Subflow Bwd Bytes",
    "Init_Win_bytes_forward",
    "Init_Win_bytes_backward",
    "act_data_pkt_fwd",
    "min_seg_size_forward",
    "Active Mean",
    "Active Std",
    "Active Max",
    "Active Min",
    "Idle Mean",
    "Idle Std",
    "Idle Max",
    "Idle Min"
]


explainer = shap.TreeExplainer(model)


class ExplainRequest(BaseModel):
    features: list[float]


@router.post("/explain")
def explain(data: ExplainRequest):

    features = np.array(
        data.features
    ).reshape(1, -1)

    attack_pred = int(
        model.predict(features)[0]
    )

    attack_type = encoder.inverse_transform(
        [attack_pred]
    )[0]

    shap_values = explainer.shap_values(
        features
    )

    sample_shap = shap_values[
        0, :, attack_pred
    ]

    importance = np.abs(
        sample_shap
    )

    top_idx = np.argsort(
        importance
    )[::-1][:10]

    top_features = []

    for idx in top_idx:
        top_features.append(
            {
                "feature":
                    feature_names[idx],
                "importance":
                    round(
                        float(
                            importance[idx]
                        ),
                        4
                    )
            }
        )

    return {
        "attack_type":
            attack_type,
        "top_features":
            top_features
    }