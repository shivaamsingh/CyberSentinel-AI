from fastapi import APIRouter
from pydantic import BaseModel
import ollama

from src.rag.rag_chat import ask_rag

router = APIRouter()


class AnalysisRequest(BaseModel):
    attack_type: str
    risk_level: str
    ip: str


mitre_map = {
    "PortScan": {
        "tactic": "Reconnaissance",
        "technique": "T1046 Network Service Discovery"
    },
    "BruteForce": {
        "tactic": "Credential Access",
        "technique": "T1110 Brute Force"
    },
    "DDoS": {
        "tactic": "Impact",
        "technique": "T1498 Network Denial of Service"
    },
    "Bot": {
        "tactic": "Command and Control",
        "technique": "T1071 Application Layer Protocol"
    },
    "WebAttack": {
        "tactic": "Initial Access",
        "technique": "T1190 Exploit Public-Facing Application"
    },
    "BENIGN": {
        "tactic": "None",
        "technique": "No malicious activity detected"
    }
}

@router.post("/analyze-threat")
def analyze_threat(data: AnalysisRequest):

    mitre = mitre_map.get(
        data.attack_type,
        {
            "tactic": "Unknown",
            "technique": "Unknown"
        }
    )

    rag_context = ask_rag(
        data.attack_type
    )

    prompt = f"""
You are a senior SOC analyst.

Threat Details:
Attack Type: {data.attack_type}
Risk Level: {data.risk_level}
Source IP: {data.ip}

MITRE ATT&CK:
Tactic: {mitre['tactic']}
Technique: {mitre['technique']}

Knowledge Base:
{rag_context}

Generate:

1. Executive Summary
2. Threat Assessment
3. MITRE ATT&CK Mapping
4. Potential Impact
5. Recommended Actions
6. Incident Response Plan

Keep the report concise and professional.
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "attack_type": data.attack_type,
        "mitre_tactic": mitre["tactic"],
        "mitre_technique": mitre["technique"],
        "analysis": response["message"]["content"]
    }