from fastapi import APIRouter

router = APIRouter()

alerts = []


@router.get("/alerts")
def get_alerts():
    return alerts