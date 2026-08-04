# 🚀 IssueLens

> AI-powered GitHub Issue Intelligence Platform that helps developers search, analyze, and understand GitHub issues using semantic search and Large Language Models (LLMs).

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Overview

GitHub repositories often contain hundreds or even thousands of issues. Finding relevant issues, identifying duplicates, and understanding historical discussions can be time-consuming.

**IssueLens** leverages AI and semantic search to make GitHub issues searchable using natural language, enabling developers and maintainers to quickly discover relevant information.

Instead of searching with keywords like:

> "authentication"

You can search naturally:

> "Why does login fail after password reset?"

IssueLens retrieves the most relevant issues based on semantic similarity rather than exact keyword matches.

---

## ✨ Features

### ✅ Current

- FastAPI Backend
- MongoDB Atlas Integration
- Environment-based Configuration
- Health Check API
- Modular Backend Architecture

### 🚧 In Development

- GitHub Repository Import
- GitHub Issues Synchronization
- Repository Dashboard
- Semantic Issue Search
- Vector Embeddings
- Duplicate Issue Detection
- AI-powered Issue Summaries
- Similar Issue Recommendations

---

## 🏗️ Architecture

```
             +----------------+
             |   Frontend     |
             +--------+-------+
                      |
                      v
             +----------------+
             |   FastAPI API  |
             +--------+-------+
                      |
          +-----------+------------+
          |                        |
          v                        v
 GitHub REST API             MongoDB Atlas
          |                        |
          +-----------+------------+
                      |
                      v
              Semantic Search
               (Coming Soon)
```

---

## 🛠️ Tech Stack

### Backend

- FastAPI
- Python 3.11
- Motor (Async MongoDB Driver)
- Pydantic v2
- HTTPX

### Database

- MongoDB Atlas

### AI (Planned)

- Sentence Transformers
- FAISS
- OpenAI / OpenRouter APIs
- LangChain (optional)

### Frontend (Upcoming)

- Next.js
- React
- Tailwind CSS

---

## 📂 Project Structure

```
IssueLens/

├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── ai/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── tests/
│   ├── pyproject.toml
│   └── README.md
│
├── frontend/
│
└── docs/
```

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/IssueLens.git

cd IssueLens/backend
```

### Install Dependencies

```bash
uv sync
```

### Configure Environment

Create a `.env` file:

```env
MONGODB_URL=your_mongodb_connection_string
DATABASE_NAME=issuelens
GITHUB_TOKEN=your_github_token
```

### Run the Backend

```bash
uv run uvicorn app.main:app --reload
```

API Documentation:

```
http://localhost:8000/docs
```

---

## 🗺️ Roadmap

### Phase 1

- [x] Backend Setup
- [x] MongoDB Atlas Integration
- [x] FastAPI Configuration
- [ ] GitHub Repository Import
- [ ] GitHub Issues Import

### Phase 2

- [ ] Semantic Search
- [ ] Issue Embeddings
- [ ] Duplicate Detection
- [ ] Repository Dashboard

### Phase 3

- [ ] AI Issue Summaries
- [ ] Issue Recommendation Engine
- [ ] RAG-based Question Answering
- [ ] Analytics Dashboard

---

## 🎯 Motivation

Maintainers of large open-source projects spend significant time:

- Searching for similar issues
- Identifying duplicate bug reports
- Understanding historical discussions
- Navigating large issue trackers

IssueLens aims to reduce this effort using AI-powered semantic search and intelligent issue analysis.

---

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Yash Bhat**

Built with ❤️ using FastAPI, MongoDB, and AI.
