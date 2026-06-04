from pathlib import Path
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

BASE_DIR = Path(__file__).parent

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=str(BASE_DIR / "chroma_db"),
    embedding_function=embeddings
)

retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

def retrieve_context(query: str):
    docs = retriever.invoke(query)

    print(f"Retrieved {len(docs)} docs")

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context