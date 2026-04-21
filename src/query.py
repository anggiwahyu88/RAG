import chromadb
import os
from dotenv import load_dotenv
from google import genai
from chromadb.utils import embedding_functions

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

CHROMA_PATH = r"chroma_db"
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

google_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
    api_key=api_key,
    model_name="models/gemini-embedding-001"
)

collection = chroma_client.get_or_create_collection(
    name="uu-ite",
    embedding_function=google_ef
)

print("🤖 Sistem Tanya Jawab UU ITE Telah Aktif!")
print("Ketik 'keluar', 'exit', atau 'quit' untuk mengakhiri percakapan.\n")

while True:
    user_query = input("========================================================\nApa yang ingin Anda tahu? (Ketik pertanyaan Anda):\n> ")
    
    if user_query.lower() in ['keluar', 'exit', 'quit', 'q']:
        print("\nTerima kasih telah menggunakan asisten hukum. Sampai jumpa!")
        break 
    
    if not user_query.strip():
        continue

    print("\nSedang mencari informasi di dalam dokumen...")
    
    results = collection.query(
        query_texts=[user_query],
        n_results=10
    )

    prompt = f"""
    Anda adalah asisten ahli hukum yang bertugas menjawab pertanyaan berdasarkan Undang-Undang Republik Indonesia Nomor 11 Tahun 2008 tentang Informasi dan Transaksi Elektronik yang telah saya berikan.

    Instruksi Kerja:
    - Jawablah pertanyaan hanya dengan menggunakan informasi yang terdapat dalam dokumen tersebut.
    - Anda diperbolehkan melakukan parafrase atau merangkum informasi agar relevan dengan pertanyaan, selama maknanya tetap sesuai dengan isi dokumen.
    - Jika pertanyaan menanyakan pasal atau bab tertentu, cari konten yang sesuai meskipun struktur kalimat pertanyaannya berbeda dengan teks asli.
    - Dilarang keras menggunakan pengetahuan eksternal di luar dokumen ini atau mengada-ada.
    - Jika jawaban benar-benar tidak ditemukan dalam dokumen tersebut, katakan: "Saya tidak tahu".
    - Sertakan nomor pasal atau ayat sebagai referensi dalam jawaban Anda.

    Data:
    {str(results['documents'])}
    --------------------
    Pertanyaan:
    {user_query}
    """

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        print("\n⚖️  Jawaban Gemini:\n")
        print(response.text)
        print("\n") 
        
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan saat menghubungi Gemini: {e}\n")