from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from chromadb.utils import embedding_functions
import chromadb
import os
from dotenv import load_dotenv
import re

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

DATA_PATH = r"data/uu-ite.pdf"
CHROMA_PATH = r"chroma_db"

embedding_function = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
    api_key=api_key, 
    model_name="models/gemini-embedding-001"
)

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = chroma_client.get_or_create_collection(
    name="uu-ite",
    embedding_function=embedding_function
)

loader = PyPDFLoader(DATA_PATH)
raw_documents = loader.load()

print("Jumlah raw documents:", len(raw_documents))

text_splitter = RecursiveCharacterTextSplitter(
  chunk_size=1000, 
  chunk_overlap=200
)

chunks = text_splitter.split_documents(raw_documents)

print("Jumlah chunks:", len(chunks))

documents = []
metadatas = []
ids = []

def extract_pasal(text):
    match = re.search(r"Pasal\s+(\d+)", text)
    if match:
        return f"Pasal {match.group(1)}"
    return "Tidak diketahui"

for i, chunk in enumerate(chunks):
    content = chunk.page_content.strip()

    if not content:
        continue

    pasal = extract_pasal(content)

    documents.append(content)
    metadatas.append({
        "pasal": pasal,
        "page": chunk.metadata.get("page", None)
    })
    ids.append(f"ID{i}")


collection.upsert(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

print("✅ Data berhasil dimasukkan ke ChromaDB!")