from fastapi import APIRouter
from pydantic import BaseModel
import ollama
from src.rag.rag_chat import ask_rag

router = APIRouter()


class InvestigationRequest(BaseModel):
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
    "DoS": {
        "tactic": "Impact",
        "technique": "T1499 Endpoint Denial of Service"
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


@router.post("/investigate")
def investigate(data: InvestigationRequest):
    # Special early return case for benign traffic
    if data.attack_type == "BENIGN":
        return {
            "attack_type": "BENIGN",
            "mitre_tactic": "None",
            "mitre_technique": "No malicious activity detected",
            "investigation": """
Executive Summary
No malicious activity detected.

Likely Attacker Goal
None identified.

Potential Impact
No security impact observed.

MITRE ATT&CK Mapping
Not applicable.

Recommended Actions
Continue normal monitoring and maintain standard security controls.
""".strip()
        }

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

Investigate this cybersecurity event.

Attack Type: {data.attack_type}
Risk Level: {data.risk_level}
Source IP: {data.ip}

MITRE ATT&CK Tactic:
{mitre['tactic']}

MITRE ATT&CK Technique:
{mitre['technique']}

Knowledge Base Context:
{rag_context}

Rules:
- Use only the MITRE information provided.
- Do not invent additional MITRE IDs.
- Do not invent threat intelligence.
- Do not invent vulnerabilities.

Provide:

1. Executive Summary
2. Likely Attacker Goal
3. Potential Impact
4. MITRE ATT&CK Mapping
5. Recommended Actions

Be concise and professional.
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
        "investigation": response["message"]["content"]
    }