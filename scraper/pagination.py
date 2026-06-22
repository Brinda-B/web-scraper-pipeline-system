import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"

def get_all_quotes():
    page_url = "/"
    all_quotes = []

    while page_url:

        response = requests.get(BASE_URL + page_url)

        soup = BeautifulSoup(response.text, "lxml")

        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:

            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text

            all_quotes.append(
                {
                    "text": text,
                    "author": author
                }
            )

        next_button = soup.find("li", class_="next")

        if next_button:
            page_url = next_button.find("a")["href"]
        else:
            page_url = None

    return all_quotes