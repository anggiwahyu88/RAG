# 🤖 RAG Starter Pack — UTS Data Engineering

> **Retrieval-Augmented Generation** — Sistem Tanya-Jawab Cerdas Berbasis Dokumen

Starter pack ini adalah **kerangka awal** proyek RAG untuk UTS Data Engineering D3/D4.


**Sistem Rekomendasi Pasal UU ITE — Sistem Rekomendasi Pasal UU ITE Berdasarkan Input Kasus**.

Proyek ini adalah implementasi sistem RAG untuk pemenuhan tugas UTS Data Engineering D4. Sistem ini dikembangkan untuk memproses input berupa deskripsi kasus dari pengguna, kemudian mencari dan merekomendasikan pasal-pasal dalam Undang-Undang Informasi dan Transaksi Elektronik (UU ITE) Tahun 2008 yang paling relevan dengan kasus tersebut.

---

## 👥 Identitas Kelompok

| Nama | NIM | Tugas Utama |
|------|-----|-------------|
| Anggi Wahyu Saputra  | 244311003 | Data Engineer         |
| Azza Auliyaul Fitri  | 244311006 | Data Analyst         |
| Prima Afda Mukhlisin  | 244311024 | Project Manager         |

**Topik Domain:** Hukum  
**Stack yang Dipilih:** LangChain  
**LLM yang Digunakan:** Gemini  
**Vector DB yang Digunakan:** ChromaDB

---

## 🗂️ Struktur Proyek

```
rag-uts-UUITE/
├── chroma_db/
│   └── chroma.sqlite3       # Vector Db
├── data/                    # Dokumen sumber (PDF, Docx)
│   ├── Persoalan-UU-ITE-dan-Pelanggan-Hak-Digital.docx
│   ├── UU Nomor 19 Tahun 2016.pdf          
│   └── uu-ite.pdf           
├── src/
│   ├── indexing.py          # 🔧 Pipeline indexing
│   └── query.py             # 🔧 Pipeline query & retrieval
├── docs/
│   └── arsitektur.png       # 📌 Diagram arsitektur
├── evaluation/
│   ├── hasil_evaluasi.pdf   # 📌 Tabel evaluasi 10 pertanyaan
│   └── hasil_evaluasi.xlsx  # 📌 Tabel evaluasi 10 pertanyaan
├── .env.example             # Template environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚡ Cara Menjalankan (Quickstart)

### 1. Clone & Setup

```bash
# Clone repository ini
git clone https://github.com/[username]/rag-uts-UUITE.git
cd rag-uts-UUITE

# Buat virtual environment
python -m venv venv
venv\Scripts\activate   

# Install dependencies
pip install -r requirements.txt
```

### 2. Konfigurasi API Key

```bash
# Salin template env
cp .env.example .env

# Edit .env dan isi API key Anda
# JANGAN commit file .env ke GitHub!
```

### 3. Siapkan Dokumen

Letakkan dokumen sumber Anda di folder `data/`:
```bash
cp uu-ite.pdf data/
cp UU Nomor 19 Tahun 2016.pdf data/
cp Persoalan-UU-ITE-dan-Pelanggan-Hak-Digital.docx data/
```

### 4. Jalankan Indexing 

```bash
python src/indexing.py
```

### 5. Jalankan Sistem RAG

```bash

# CLI
python src/query.py
```

---

## 🔧 Konfigurasi

Semua konfigurasi utama ada di `src/config.py` (atau langsung di setiap file):

| Parameter | Default | Keterangan |
|-----------|---------|------------|
| `CHUNK_SIZE` | 1000 | Ukuran setiap chunk teks (karakter) |
| `CHUNK_OVERLAP` | 200 | Overlap antar chunk |
| `TOP_K` | 3 | Jumlah dokumen relevan yang diambil |
| `MODEL_NAME` | Gemini | Nama model LLM yang digunakan |

---

---

## 🏗️ Arsitektur Sistem


<img width="714" height="301" alt="arsitektur" src="https://github.com/user-attachments/assets/a55813b7-6b84-4cbd-ba94-5381d26c0cb4" />



---


## 📚 Referensi & Sumber

- Framework: LangChain docs
- LLM: Gemini
- Vector DB: ChromaDB
- Tutorial yang digunakan: (https://github.com/ThomasJanssen-tech/Retrieval-Augmented-Generation.git)

---

## 👨‍🏫 Informasi UTS

- **Mata Kuliah:** Data Engineering
- **Program Studi:** D4 Teknologi Rekayasa Perangkat Lunak
- **Deadline:** 23 April 2026
