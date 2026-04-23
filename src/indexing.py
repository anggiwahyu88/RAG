from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from chromadb.utils import embedding_functions
import chromadb
import os
from dotenv import load_dotenv
import re

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

DATA_DIR = r"data" 
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

raw_documents = []

for file_name in os.listdir(DATA_DIR):
    file_path = os.path.join(DATA_DIR, file_name)
    
    if file_name.endswith(".pdf"):
        print(f"Loading PDF: {file_name}")
        loader = PyPDFLoader(file_path)
        raw_documents.extend(loader.load())
        
    elif file_name.endswith(".docx"):
        print(f"Loading DOCX: {file_name}")
        loader = Docx2txtLoader(file_path)
        raw_documents.extend(loader.load())

print("\nJumlah total halaman/raw documents:", len(raw_documents))

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200
)

chunks = text_splitter.split_documents(raw_documents)

print("Jumlah chunks yang akan diproses:", len(chunks))

documents = []
metadatas = []
ids = []

def extract_pasal(text):
    match = re.search(r"Pasal\s+(\d+)", text, re.IGNORECASE)
    if match:
        return f"Pasal {match.group(1)}"
    return "Tidak diketahui"

for i, chunk in enumerate(chunks):
    content = chunk.page_content.strip()

    if not content:
        continue

    pasal = extract_pasal(content)
    
    source_file = chunk.metadata.get("source", "Unknown")

    documents.append(content)
    metadatas.append({
        "pasal": pasal,
        "page": chunk.metadata.get("page", 0), 
        "source": source_file
    })
    ids.append(f"ID_ALL_{i}") 

print("Jumlah documents siap insert:", len(documents))

print("Sedang melakukan proses embedding dan penyimpanan (mohon tunggu)...")
collection.upsert(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

print("✅ Data dari berbagai dokumen berhasil dimasukkan ke ChromaDB!")