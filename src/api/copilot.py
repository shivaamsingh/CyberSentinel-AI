from fastapi import APIRouter
from pydantic import BaseModel
import ollama

router = APIRouter()

class CopilotRequest(BaseModel):
    question: str

@router.post("/copilot")
def copilot(data: CopilotRequest):

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert cybersecurity analyst. "
                    "Answer cybersecurity questions clearly and accurately."
                )
            },
            {
                "role": "user",
                "content": data.question
            }
        ]
    )

    return {
        "answer": response["message"]["content"]
    }