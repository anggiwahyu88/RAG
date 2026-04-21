# 🤖 RAG Starter Pack — UTS Data Engineering

> **Retrieval-Augmented Generation** — Sistem Tanya-Jawab Cerdas Berbasis Dokumen

Starter pack ini adalah **kerangka awal** proyek RAG untuk UTS Data Engineering D3/D4.
Mahasiswa mengisi, memodifikasi, dan mengembangkan kode ini sesuai topik kelompok masing-masing.

---

## 👥 Identitas Kelompok

| Nama | NIM | Tugas Utama |
|------|-----|-------------|
| Anggi Wahyu Saputra  | 244311003 | ...         |
| Azza Auliyaul Fitri  | 244311006 | ...         |
| Prima Afda Mukhlisin  | 244311004 | ...         |

**Topik Domain:** Hukum 
**Stack yang Dipilih:** LangChain
**LLM yang Digunakan:** Gemini  
**Vector DB yang Digunakan:** ChromaDB

---

## 🗂️ Struktur Proyek

```
rag-uts-[RAG-uu-ite]/
├── data/                    
│   └── uu-ite.pdf           
├── src/
│   ├── indexing.py         
│   └── query.py             
├── ui/
│   └── app.py               
├── docs/
│   └── arsitektur.png       
├── evaluation/
│   └── hasil_evaluasi.xlsx  
├── notebooks/
│   └── 01_demo_rag.ipynb    
├── .env.example             
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔧 Konfigurasi

Semua konfigurasi utama ada di `src/config.py` (atau langsung di setiap file):

| Parameter | Default | Keterangan |
|-----------|---------|------------|
| `CHUNK_SIZE` | 1000 | Ukuran setiap chunk teks (karakter) |
| `CHUNK_OVERLAP` | 200 | Overlap antar chunk |
| `TOP_K` | 1 | Jumlah dokumen relevan yang diambil |
| `MODEL_NAME` | Gemini | Nama model LLM yang digunakan |

---

## 📊 Hasil Evaluasi

*(Isi setelah pengujian selesai)*

| # | Pertanyaan | Jawaban Sistem | Jawaban Ideal | Skor (1-5) |
|---|-----------|----------------|---------------|-----------|
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |

**Rata-rata Skor:** ...  
**Analisis:** ...

---

## 🏗️ Arsitektur Sistem

*(Masukkan gambar diagram arsitektur di sini)*

```
[Dokumen] → [Loader] → [Splitter] → [Embedding] → [Vector DB]
                                                         ↕
[User Query] → [Query Embed] → [Retriever] → [Prompt] → [LLM] → [Jawaban]
```

---

## 📚 Referensi & Sumber

- Framework: LangChain docs 
- LLM: Gemini
- Vector DB: ChromaDB
- Tutorial yang digunakan: *(cantumkan URL)*

---

## 👨‍🏫 Informasi UTS

- **Mata Kuliah:** Data Engineering
- **Program Studi:** D4 Teknologi Rekayasa Perangkat Lunak
- **Deadline:** 23 April 2026
