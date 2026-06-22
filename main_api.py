from fastapi import FastAPI
from database.db import get_connection
from database.models import fetch_all_quotes
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Web Scraper API is running"}

@app.get("/quotes")
def get_quotes():
    return fetch_all_quotes()

@app.get("/quotes/random")
def get_random_quote():
    quotes = fetch_all_quotes()
    return random.choice(quotes) if quotes else {"error": "No quotes found"}

@app.post("/scrape")
def scrape():
    try:
        from scraper.scraper import run_scraper
        run_scraper()
        return {
            "message": "Scraping completed",
            "status": "success"
        }
    except Exception as e:
        return {"error": str(e)} 