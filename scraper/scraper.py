import sys
import os
import requests
from bs4 import BeautifulSoup

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from database.models import insert_quote
from utils.logger import log

url = "https://quotes.toscrape.com/"

log("Scraper started")

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "lxml")

    quotes = soup.find_all("div", class_="quote")

    print(f"Found {len(quotes)} quotes")

    for quote in quotes:

        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

        insert_quote(text, author)

        log(f"Inserted quote by {author}")

        print(f"Saved: {author}")

    log("Scraper completed successfully")

else:
    log("Failed to fetch website")
    print("Failed to fetch website")