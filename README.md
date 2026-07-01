# Local_Document_Chat_Assistant

# 🧠 LocalRAG-Ollama

An offline Retrieval-Augmented Generation (RAG) application built with LangChain, Ollama, ChromaDB, and Gemma 3.

This project allows users to chat with their own documents completely offline. Documents are converted into vector embeddings using `nomic-embed-text`, stored in ChromaDB, retrieved based on semantic similarity, and finally answered by Gemma 3 running locally through Ollama.

---

## 🚀 Features

- 📄 Document ingestion from text files
- ✂️ Automatic document chunking
- 🧠 Local embeddings using Ollama (`nomic-embed-text`)
- 📚 Persistent Chroma Vector Database
- 🔍 Semantic similarity search
- 💬 Conversational RAG with chat history
- 🤖 Local LLM using Gemma 3
- 🔒 Completely offline (No OpenAI API required)

---

## 🏗️ Architecture

```

User Question
│
▼
Chat History
│
▼
Question Rewriter (Gemma 3)
│
▼
Embedding (nomic-embed-text)
│
▼
Chroma Vector Database
│
▼
Top-K Retrieved Documents
│
▼
Gemma 3
│
▼
Final Answer



🛠️ Tech Stack
Python
LangChain
Ollama
Gemma 3
nomic-embed-text
ChromaDB
dotenv
📂 Project Structure
LocalRAG-Ollama/
│
├── docs/
│   ├── ai.txt
│   ├── coffee.txt
│   ├── mars.txt
│   ├── quantum.txt
│   └── renewable.txt
│
├── db/
│   └── chrom_db/
│
├── ingestion_pipeline.py
├── retrieval_pipeline.py
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Installation

Clone the repository

git clone https://github.com/<your_username>/LocalRAG-Ollama.git

cd LocalRAG-Ollama

Create a virtual environment

python -m venv .venv

Activate it

Windows

.venv\Scripts\activate

Linux / macOS

source .venv/bin/activate

Install dependencies

pip install -r requirements.txt
📥 Install Ollama

Download and install Ollama from

https://ollama.com/

Pull the required models

ollama pull gemma3:4b

ollama pull nomic-embed-text
📄 Add Documents

Place your .txt files inside

docs/

Example

docs/
    ai.txt
    mars.txt
    renewable.txt
📚 Create the Vector Database

Run

python ingestion_pipeline.py

This will

Load documents
Split them into chunks
Generate embeddings
Store them in ChromaDB
💬 Start Chatting
python retrieval_pipeline.py

Example

You:
Where did Perseverance land?

Assistant:
NASA's Perseverance rover landed in Jezero Crater in 2021.
📌 Example Questions
What is superposition?
What are the two types of coffee beans?
Where did Perseverance land?
What is Artificial Intelligence?
What are photovoltaic cells?
Compare renewable energy with fossil fuels.
