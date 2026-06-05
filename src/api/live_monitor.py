from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

live_alerts = []


class Alert(BaseModel):
    alert: str
    pps: float
    bps: float


@router.get("/live-alerts")
def get_live_alerts():
    return live_alerts


@router.post("/push-alert")
def push_alert(alert: Alert):

    live_alerts.append({
    "timestamp": datetime.now().strftime("%H:%M:%S"),
    "alert": alert.alert,
    "pps": alert.pps,
    "bps": alert.bps
})

    if len(live_alerts) > 20:
        live_alerts.pop(0)

    return {
        "status": "ok"
    }