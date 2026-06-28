# ABC Technologies Customer Support Automation System

## Overview

This project is an AI-powered Customer Support Automation System developed using LangGraph.

The system automates customer support by:

- Classifying customer queries
- Routing them to specialized support agents
- Retrieving information from company documents using RAG
- Maintaining conversation history using SQLite
- Escalating sensitive requests to a human supervisor
- Generating professional customer responses

---

## Features

- Intent Classification
- Conditional Routing
- Sales Agent
- Technical Agent
- Billing Agent
- Account Agent
- Memory Agent
- Retrieval-Augmented Generation (FAISS)
- SQLite Memory
- Human-in-the-Loop Approval
- Supervisor Agent

---

## Folder Structure

customer-support-bot/
│
├── app.py
├── requirements.txt
├── README.md
├── agents/
├── graph/
├── rag/
├── human/
├── memory/
├── documents/

---

## Installation

```bash
pip install -r requirements.txt
```

Create `.env`

```
GROQ_API_KEY=your_api_key
```

---

## Build Vector Database

```bash
python build_vectorstore.py
```

---

## Run

```bash
python app.py
```

---

## Technologies Used

- LangGraph
- LangChain
- Groq
- FAISS
- HuggingFace Embeddings
- SQLite
- Python
