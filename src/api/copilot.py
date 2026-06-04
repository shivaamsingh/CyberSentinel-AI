from fastapi import APIRouter

router = APIRouter()

@router.get("/copilot")
def copilot(query: str):

    query = query.lower()

    if "ddos" in query:
        return {
            "answer":
            "A DDoS attack floods a target with malicious traffic, making services unavailable to legitimate users."
        }

    if "portscan" in query:
        return {
            "answer":
            "Port scanning is a reconnaissance technique used to discover open ports and vulnerable services."
        }

    if "bruteforce" in query:
        return {
            "answer":
            "A brute force attack repeatedly attempts passwords until valid credentials are found."
        }

    if "anomaly" in query:
        return {
            "answer":
            "An anomaly is unusual network behavior that deviates from expected traffic patterns."
        }

    return {
        "answer":
        "I do not have information about that threat yet."
    }