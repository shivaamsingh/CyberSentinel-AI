from fastapi import APIRouter
from pydantic import BaseModel
from ollama import Client

router = APIRouter()

client = Client(
    host="http://ollama:11434"
)


class CopilotRequest(BaseModel):
    question: str


@router.post("/copilot")
def copilot(data: CopilotRequest):

    response = client.chat(
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