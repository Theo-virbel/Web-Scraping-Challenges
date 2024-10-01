import requests
from bs4 import BeautifulSoup
import time

def scrape_quotes():
    start_time = time.time()  # Démarre le chronomètre
    quotes = []
    page_number = 1

    while True:
        url = f"https://quotes.toscrape.com/page/{page_number}/"
        response = requests.get(url)

        if response.status_code != 200:
            break  # Arrête si la page n'existe pas

        soup = BeautifulSoup(response.text, 'html.parser')
        quotes_on_page = soup.find_all(class_='quote')

        if not quotes_on_page:
            break  # Arrête si aucune citation trouvée

        for quote in quotes_on_page:
            text = quote.find(class_='text').get_text()
            author = quote.find(class_='author').get_text()
            quotes.append({'text': text, 'author': author})

        page_number += 1

    end_time = time.time()  # Arrête le chronomètre
    duration = end_time - start_time
    return duration

scraping_time = scrape_quotes()
print(f"Temps de scraping : {scraping_time} secondes")
