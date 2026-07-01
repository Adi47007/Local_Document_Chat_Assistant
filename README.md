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
