# 🤖 Sherry – AI Assistant V1

> A modern AI-powered chat application built with **FastAPI** and a clean **HTML/CSS/JavaScript** frontend, designed as the first milestone in a long-term AI Engineering journey.

---

# 📖 Overview

Sherry is an AI assistant that provides an intuitive chat experience through a clean web interface. The project focuses on building a production-style AI application by integrating Large Language Models (LLMs) with a scalable backend architecture.

This is **Version 1** of Sherry, which establishes the core chat functionality. Future versions will progressively introduce Retrieval-Augmented Generation (RAG), voice interaction, AI agents, and multi-model orchestration.

---

# ✨ Features

* 💬 Real-time AI chat interface
* 🎨 Clean and responsive UI
* ⚡ FastAPI backend
* 🔍 Chat history support
* 📱 Mobile-friendly design
* 🔐 Environment variable support for API keys
* 🧩 Modular project structure
* 🚀 Easy to extend with new AI models

---

# 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* FastAPI
* Uvicorn
* Python

### AI

* Google Gemini API *(current)*
* Designed for future support of multiple LLM providers

---

# 🏗️ Architecture

```
                User
                  │
                  ▼
        HTML / CSS / JavaScript
                  │
                  ▼
            FastAPI Backend
                  │
                  ▼
          AI Model (Gemini API)
                  │
                  ▼
              AI Response
                  │
                  ▼
               Chat UI
```

---

# 📂 Project Structure

```
Sherry/
│
├── backend/
│   ├── app/
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── config/
│   ├── utils/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── index.html
│
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/sherry.git

cd sherry
```

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file.

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## 5. Run the backend

```bash
uvicorn app.main:app --reload
```

---

## 6. Open the frontend

Launch `index.html` in your browser or serve the frontend using your preferred local server.

---

# 🚀 Future Roadmap

## ✅ Version 1

* Chat interface
* FastAPI backend
* Gemini integration
# Just had completed Version and need to commited more.
## 🔄 Version 2     

* Retrieval-Augmented Generation (RAG)
* PDF upload
* Vector database
* Semantic search

## 🎤 Version 3

* Voice input
* Voice output
* Speech-to-text
* Text-to-speech

## 🤖 Version 4

* AI Agents
* Tool calling
* Web search
* Memory
* Multi-step reasoning

## 🌐 Version 5

* Multi-model routing
* Multi-agent collaboration
* Production deployment
* Monitoring and observability

---

# 📸 Screenshots

> Add screenshots of the application here.

Example:

```
screenshots/
├── home.png
├── chat.png
└── mobile.png
```

---

# 🎯 Learning Goals

This project is part of a progressive AI Engineering roadmap focused on learning by building real-world applications.

Topics explored include:

* FastAPI
* REST APIs
* Prompt Engineering
* LLM Integration
* Frontend Development
* Production Project Structure
* AI System Design

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub. It helps others discover the project and motivates continued development.

Happy Building! 🚀
