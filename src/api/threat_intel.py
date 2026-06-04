from fastapi import APIRouter

router = APIRouter()


@router.get("/threat-intel/{ip}")
def lookup_ip(ip: str):

    mock_db = {
        "8.8.8.8": {
            "risk_score": 10,
            "status": "CLEAN"
        },
        "1.1.1.1": {
            "risk_score": 5,
            "status": "CLEAN"
        },
        "192.168.1.100": {
            "risk_score": 85,
            "status": "SUSPICIOUS"
        }
    }

    return mock_db.get(
        ip,
        {
            "risk_score": 50,
            "status": "UNKNOWN"
        }
    )