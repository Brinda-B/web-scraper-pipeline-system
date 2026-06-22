# Web Scraper Pipeline System

## Overview

A Python-based web scraping and data pipeline system that extracts quote data from a website, processes it, and stores it in PostgreSQL. The system also exposes the data through a FastAPI REST API for retrieval and automation.

---

## Features

- Web scraping using Requests and BeautifulSoup
- Multi-page scraping with pagination support
- PostgreSQL database integration
- Duplicate record prevention
- Logging system for debugging and monitoring
- REST API using FastAPI
- API-triggered scraping pipeline

---

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Requests
- BeautifulSoup4
- PostgreSQL
- psycopg2

---

## Project Structure

```text
web-scraper-pipeline-system/
│
├── scraper/
│   ├── scraper.py
│   ├── pagination.py
│   └── test_pagination.py
│
├── database/
│   ├── __init__.py
│   ├── db.py
│   ├── models.py
│   ├── test_connection.py
│   └── test_insert.py
│
├── utils/
│   └── logger.py
│
├── logs/
│   └── app.log (auto-generated)
│
├── main_api.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/quotes` | Fetch all quotes |
| GET | `/quotes/random` | Fetch a random quote |
| POST | `/scrape` | Trigger web scraping pipeline |

---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start FastAPI server
```bash
python -m uvicorn main_api:app --reload
```

### 3. Open API docs
```
http://127.0.0.1:8000/docs
```

---

## Key Learnings

- Web scraping and structured data extraction
- Backend API development using FastAPI
- PostgreSQL database design and operations
- Modular Python project architecture
- Logging and debugging techniques
- Git and version control workflow

---

## Future Improvements

- Add scheduled scraping (automation)
- Deploy API using cloud platforms (Render/Railway)
- Add authentication for API security
- Containerize project using Docker

---

## Author

Brinda B
