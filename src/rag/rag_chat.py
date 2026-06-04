from src.rag.retriever import retrieve_context
import os

os.environ["OLLAMA_NO_GPU"] = "1"

import ollama


def ask_rag(question: str):

    context = retrieve_context(question)

    prompt = f"""
You are a cybersecurity expert.

Use ONLY the provided context to answer.

Context:
{context}

Question:
{question}

Answer:
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

    return response["message"]["content"]