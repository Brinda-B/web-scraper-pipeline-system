# Web Scraper Pipeline System

## Overview

A Python-based web scraping and data pipeline system that extracts quote data from a website, processes it, and stores it in PostgreSQL for analysis and retrieval.

## Features

- Web scraping using Requests and BeautifulSoup
- Multi-page scraping with pagination
- PostgreSQL database integration
- Duplicate prevention
- Logging support
- Modular project structure

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- PostgreSQL
- psycopg2

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
│
├── config.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

```bash
pip install -r requirements.txt
python scraper/scraper.py
```

## Key Learnings

- Web scraping and data extraction
- PostgreSQL database operations
- Python backend development
- Logging and debugging
- Git and GitHub workflow

## Author

Brinda B
