from fastapi import APIRouter
from ollama import Client
from pydantic import BaseModel

from src.rag.rag_chat import ask_rag

router = APIRouter()
client = Client(
    host="http://ollama:11434"
)

class RAGRequest(BaseModel):
    question: str


@router.post("/rag-chat")
def rag_chat(data: RAGRequest):

    answer = ask_rag(
        data.question
    )

    return {
        "answer": answer
    }