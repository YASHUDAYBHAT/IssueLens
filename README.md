# 🔍 IssueLens

> AI-powered GitHub Repository Intelligence Platform for semantic code search, repository indexing, and intelligent issue analysis.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen)
![Sentence Transformers](https://img.shields.io/badge/Embeddings-MiniLM-orange)
![FAISS](https://img.shields.io/badge/Vector%20Search-FAISS-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📖 Overview

Modern software repositories contain thousands of files, functions, and GitHub issues. Finding the right implementation or understanding how a feature works often requires manually searching through large codebases.

**IssueLens** is an AI-powered code intelligence platform that indexes GitHub repositories, extracts code structure using Abstract Syntax Trees (AST), generates semantic embeddings, and enables natural-language search over source code.

Instead of searching with keywords like:

> `timedelta`

Developers can ask:

> "Where is time converted into a timedelta?"

IssueLens understands the meaning of the query and retrieves the most relevant code using vector similarity search.

---

# ✨ Current Features

## Repository Management

- Import GitHub repositories
- Clone repositories locally
- GitHub REST API integration
- MongoDB Atlas metadata storage

## Code Intelligence

- AST-based Python parser
- Function extraction
- Class extraction
- Method detection
- Qualified symbol names
- Source code chunk extraction
- Docstring extraction

## AI Search

- Semantic code embeddings
- SentenceTransformer (all-MiniLM-L6-v2)
- FAISS vector indexing
- Natural language code search
- Cosine similarity ranking

## Backend

- FastAPI
- MongoDB Atlas
- Modular architecture
- Environment configuration
- Async services
- Health monitoring

---

# 🚧 Upcoming Features

- GitHub Issue Import
- Semantic Issue Search
- Duplicate Issue Detection
- AI-generated Issue Summaries
- Repository Knowledge Graph
- RAG-based Question Answering
- Multi-language Support
- Incremental Repository Indexing
- Web Dashboard
- LLM-powered Code Explanations

---

# 🏗 Architecture

```text
                GitHub Repository
                        │
                        ▼
                 Git Clone Service
                        │
                        ▼
                 AST Python Parser
                        │
                        ▼
                  Code Chunks
                        │
                        ▼
           SentenceTransformer Embeddings
                        │
                        ▼
                 FAISS Vector Index
                        │
                        ▼
             Semantic Code Search API
                        │
                        ▼
                  FastAPI Backend
                        │
                        ▼
                    React Frontend
```

---

# 🛠 Tech Stack

## Backend

- FastAPI
- Python 3.11
- Motor
- HTTPX
- Pydantic v2

## Database

- MongoDB Atlas

## AI & Search

- Sentence Transformers
- all-MiniLM-L6-v2
- FAISS
- NumPy

## Git Integration

- GitPython
- GitHub REST API

## Frontend (Upcoming)

- Next.js
- React
- Tailwind CSS

---

# 📂 Project Structure

```text
IssueLens/

├── backend/
│
│   ├── app/
│   │
│   ├── api/
│   │   └── routes/
│   │
│   ├── core/
│   ├── db/
│   ├── indexing/
│   │   ├── chunker.py
│   │   ├── embedder.py
│   │   ├── utils.py
│   │   └── vector_store.py
│   │
│   ├── models/
│   ├── parsers/
│   ├── repositories/
│   ├── services/
│   │
│   └── main.py
│
├── storage/
│   └── repos/
│
├── frontend/
│
└── docs/
```

---

# 🚀 Getting Started

## Clone

```bash
git clone https://github.com/YOUR_USERNAME/IssueLens.git

cd IssueLens/backend
```

---

## Install

```bash
pip install -r requirements.txt
```

or

```bash
pip install -e .
```

---

## Environment

Create `.env`

```env
MONGODB_URL=

DATABASE_NAME=issuelens

GITHUB_TOKEN=
```

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# 🔍 Example Semantic Search

Instead of searching:

```text
timedelta
```

Developers can search:

```text
convert seconds into timedelta
```

IssueLens returns:

```text
_make_timedelta()

Similarity: 0.60

storage/repos/pallets__flask/src/flask/app.py

Lines 73-77
```

without relying on keyword matching.

---

# 📈 Roadmap

## Phase 1 ✅

- [x] FastAPI Backend
- [x] MongoDB Atlas
- [x] GitHub Repository Import
- [x] Git Repository Cloning
- [x] AST-based Python Parser
- [x] Code Chunk Extraction
- [x] SentenceTransformer Embeddings
- [x] FAISS Semantic Search

---

## Phase 2 🚧

- [ ] Repository Index API
- [ ] Search API
- [ ] GitHub Issue Import
- [ ] Issue Embeddings
- [ ] Similar Issue Detection
- [ ] AI Issue Summaries

---

## Phase 3 🚀

- [ ] Repository Dashboard
- [ ] RAG Question Answering
- [ ] LLM Code Explanation
- [ ] Multi-language Parsing
- [ ] Incremental Re-indexing
- [ ] Analytics Dashboard

---

# 🎯 Motivation

Developers spend significant time:

- Searching unfamiliar codebases
- Understanding large repositories
- Finding relevant implementations
- Connecting GitHub issues to source code
- Navigating thousands of functions

IssueLens reduces this effort by combining AST parsing, vector embeddings, semantic search, and AI-powered code understanding into a unified developer platform.

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/my-feature
```

3. Commit your changes

```bash
git commit -m "feat: add awesome feature"
```

4. Push

```bash
git push origin feature/my-feature
```

5. Open a Pull Request

---

# 📄 License

MIT License

---

# 👨‍💻 Author

**Yash Bhat**

Built with ❤️ using Python, FastAPI, MongoDB, FAISS, and AI.
