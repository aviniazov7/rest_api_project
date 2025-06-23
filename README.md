# 🔗 REST API Project — FastAPI Duo System

## 📌 What is This?

A modern, distributed system with **2 REST APIs** built in Python using **FastAPI**:

* 🧠 **Data Provider** — serves protected JSON data
* 🤖 **Consumer** — fetches data via HTTP with authentication

---

## ⚙️ Key Features

| 🔐 Security  | ✅ Basic Auth + API Key               |
| ------------ | ------------------------------------ |
| 📄 Docs      | Auto-generated (Swagger)             |
| 🔁 Structure | Fully modular & clear                |
| 🌍 REST      | Clean communication between services |

---

## 🧱 Architecture

```
Client
  │
  ▼
Consumer  ──▶  Data Provider (with auth)
             └─▶ Returns JSON
```

---

## 🚀 How to Run

📁 In your main project folder:

### 1. Start Data Provider

```bash
uvicorn data_server.main:app --reload --port 8001
```

👉 [http://localhost:8001/docs](http://localhost:8001/docs)

### 2. Start Consumer Server

```bash
uvicorn consumer_server.main:app --reload --port 8000
```

👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧩 Folder Structure

```
rest_api_project/
├── data_server/      ← FastAPI + Auth + Data
├── consumer_server/  ← FastAPI client with /fetch-data
├── .env              ← Secrets (API key, URLs)
├── requirements.txt
└── README.md
```

---

## 📦 Tech Stack

* 🐍 Python 3.9+
* ⚡ FastAPI
* 🔌 Requests
* 🔐 python-dotenv
* 🚀 Uvicorn

רוצה שאשלח לך את זה גם בקובץ `.md` מוכן להדבקה?
