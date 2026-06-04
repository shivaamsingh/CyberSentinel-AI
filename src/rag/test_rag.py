from src.rag.rag_chat import ask_rag

question = "What is SQL Injection?"

answer = ask_rag(question)

print("\nANSWER:\n")
print(answer)