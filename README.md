# Web Scraper Pipeline System

A Python-based web scraping and data pipeline system that extracts quotes from a website, processes them, and stores them in a PostgreSQL database. The project also exposes a FastAPI backend to trigger scraping and retrieve stored data.

---

## Features

- Web scraping using Requests and BeautifulSoup
- Multi-page scraping (pagination support)
- REST API using FastAPI
- PostgreSQL database integration
- Duplicate data prevention
- Logging system for debugging and tracking
- Modular and scalable architecture
- Environment variable support using `.env`

---

## Tech Stack

- Python
- FastAPI
- Requests
- BeautifulSoup4
- PostgreSQL
- psycopg2
- python-dotenv
- Uvicorn

---

## Project Structure

```text
web-scraper-pipeline-system/
│
├── scraper/                # Web scraping logic
│   ├── scraper.py
│   ├── pagination.py
│
├── database/               # Database layer
│   ├── db.py
│   ├── models.py
│
├── utils/                  # Logger utility
│   └── logger.py
│
├── logs/                   # Runtime logs (ignored in Git)
│   └── app.log
│
├── main_api.py            # FastAPI entry point
├── config.py              # Loads environment variables
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (NOT pushed to GitHub)
├── .gitignore
└── README.md
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

## Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Create `.env` file
```
Create a `.env` file in the root directory and add:

DB_HOST=localhost  
DB_NAME=scraper_db  
DB_USER=postgres  
DB_PASSWORD=your_password  
DB_PORT=5432  
```

### 3. Run the FastAPI server
```bash
python -m uvicorn main_api:app --reload
```

### 4. Open API documentation
```
http://127.0.0.1:8000/docs
```

---

## Workflow

FastAPI → Scraper → BeautifulSoup → PostgreSQL → API Response

---

## Security

- Sensitive credentials stored in `.env`
- `.env` and logs excluded using `.gitignore`
- No hardcoded passwords in code

---

## Key Learnings

- Web scraping using Requests and BeautifulSoup
- Parsing and extracting structured data from HTML
- Building REST APIs using FastAPI
- PostgreSQL database integration
- Duplicate prevention logic
- Modular backend architecture design
- Environment variable management using `.env`
- Logging and debugging in Python applications

---

## Future Improvements

- Add JWT authentication for secure APIs
- Implement scheduled scraping (cron jobs / background tasks)
- Deploy using Render / Railway / AWS
- Add frontend dashboard for visualization
- Improve scalability with async scraping (asyncio / httpx)
- Add analytics layer for insights and trends
- Add pagination API for better data access

---

## Author

Brinda B
