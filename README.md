# RAG Guardian — AI Agent Security and Data-Leakage Tester

RAG Guardian is a beginner-friendly GenAI security testing project that evaluates a Retrieval-Augmented Generation (RAG) application for prompt injection, unauthorized data access, sensitive-data leakage, and unsupported answers.

## Features

- RAG pipeline using LangChain and ChromaDB
- LLM integration using the Groq API
- Basic direct and indirect prompt-injection tests
- Document retrieval with access metadata
- Security findings with evidence and recommendations
- LangGraph-based security workflow
- FastAPI endpoints for running scans
- Streamlit dashboard for interactive testing
- Automated tests using pytest
- JSON report export

## Tech Stack

Python, LangChain, LangGraph, ChromaDB, Groq, FastAPI, Streamlit, pytest, Sentence Transformers.

## Project Structure


rag-guardian/
├── app.py
├── api.py
├── test_app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md


## Setup

### 1. Clone the repository


git clone YOUR_GITHUB_REPOSITORY_URL
cd rag-guardian


### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the Groq API

Create a `.env` file using `.env.example` as a template, then add your Groq API key.

Never commit your `.env` file.

### 5. Run the Streamlit dashboard

```bash
streamlit run app.py
```

### 6. Run the FastAPI service

Open a second terminal and activate the virtual environment:

```bash
uvicorn api:api --reload
```

Open `http://127.0.0.1:8000/docs` to access the API documentation.

### 7. Run automated tests

```bash
python -m pytest -v
```

## Current Limitations

This is an educational prototype. Its security checks are basic and do not guarantee protection against all attacks. Citation validation, robust adversarial evaluation, authenticated access control, and before-and-after defence comparisons require further development.

## Future Improvements

- PDF and document uploads
- Stronger prompt-injection evaluation
- User-level access-control tests
- Citation and factual-grounding validation
- Baseline versus defended system comparison
- Risk scoring and improved security reports
- CI testing with GitHub Actions

## Security

Use synthetic data during testing. Store API keys in environment variables and never commit credentials or confidential documents.
