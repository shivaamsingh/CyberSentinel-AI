from fastapi import APIRouter
from ollama import Client
from pydantic import BaseModel

router = APIRouter()
client = Client(
    host="http://ollama:11434"
)

class IncidentRequest(BaseModel):
    attack_type: str
    risk_level: str
    threat_score: int
    ip: str


@router.post("/generate-report")
def generate_report(data: IncidentRequest):

    # Early exit for benign traffic to simulate real SOC logic
    if data.attack_type == "BENIGN":
        return {
            "report": (
                "No security incident detected.\n\n"
                f"Attack Type: {data.attack_type}\n"
                f"Risk Level: {data.risk_level}\n"
                f"Threat Score: {data.threat_score}\n\n"
                "Traffic classified as normal network activity."
            )
        }

    prompt = f"""
You are a professional SOC (Security Operations Center) analyst.

Generate a cybersecurity incident report using ONLY the provided information.
Format the report as plain professional text.
Do not use markdown headings (#, ##, ###).

Known Facts:
- Attack Type: {data.attack_type}
- Risk Level: {data.risk_level}
- Threat Score: {data.threat_score}
- IP Address: {data.ip}

Strict Rules:
- Use only the information explicitly provided.
- Do NOT infer ownership of IP addresses.
- Do NOT identify organizations behind IP addresses.
- Do NOT invent dates.
- Do NOT invent incident IDs.
- Do NOT invent locations.
- Do NOT invent victim organizations.
- Do NOT invent technical details that are not provided.
- If information is unavailable, omit it instead of writing "Unknown".
- Keep the report concise, professional, and SOC-oriented.

Report Structure:

# Executive Summary
Brief overview of the detected threat.

# Threat Assessment
Attack type, risk level, threat score, and observed indicators.

# Potential Impact
Possible security implications based on the provided threat type.

# Recommended Actions
Provide 4-6 actionable security recommendations.

# Conclusion
Short summary of the incident and recommended next steps.
"""

    response = client.chat(
        model="llama3",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a senior cybersecurity analyst who writes "
                    "professional incident reports."
                ),
            },
            {"role": "user", "content": prompt},
        ],
    )

    return {"report": response["message"]["content"]}