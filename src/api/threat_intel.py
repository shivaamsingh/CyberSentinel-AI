from fastapi import APIRouter
from dotenv import load_dotenv
import requests
import os

load_dotenv()

router = APIRouter()

API_KEY = os.getenv(
    "ABUSEIPDB_API_KEY"
)

@router.get("/threat-intel/{ip}")
def lookup_ip(ip: str):

    url = (
        "https://api.abuseipdb.com/api/v2/check"
    )

    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=15
    )

    data = response.json()["data"]

    risk_score = data["abuseConfidenceScore"]

    threat_level = "LOW"

    if risk_score >= 50:
        threat_level = "MEDIUM"

    if risk_score >= 80:
        threat_level = "HIGH"

    return {
    "ip": data["ipAddress"],
    "risk_score": risk_score,
    "country": data.get("countryCode"),
    "reports": data["totalReports"],
    "threat_level": threat_level
}