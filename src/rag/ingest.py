from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

DOCS_DIR = BASE_DIR / "documents"

documents = []

for file in os.listdir(DOCS_DIR):
    if file.endswith(".txt"):
        loader = TextLoader(
            os.path.join(DOCS_DIR, file)
        )
        documents.extend(
            loader.load()
        )

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(
    documents
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory=str(BASE_DIR / "chroma_db")
)

print("Knowledge base created.")
print(f"Loaded {len(documents)} documents")

for doc in documents:
    print("-----")
    print(doc.page_content)

print(f"Created {len(chunks)} chunks")