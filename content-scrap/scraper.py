import requests
from bs4 import BeautifulSoup

def scrape_techcrunch():
    url = "https://techcrunch.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    headlines = []
    for headline_tag in soup.find_all("h3", class_="loop-card__title"): # Use the correct tag and class
        headline = headline_tag.text.strip()
        link = headline_tag.find("a")["href"]  # Get the link to the article
        headlines.append((headline, link))  # Store headline and link

    return headlines