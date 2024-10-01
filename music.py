import requests
from bs4 import BeautifulSoup

# URL de la page de recherche
url = "https://quotes.toscrape.com/search.aspx"

# Définir les données à envoyer avec le POST
payload = {
    'author': 'Albert Einstein',
    'tag': 'music',
    'submit_button': 'Search'
}

# Envoyer une requête POST
response = requests.post(url, data=payload)

# Vérifier que la requête a réussi
if response.status_code == 200:
    # Parser le contenu HTML de la page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Trouver les citations correspondantes
    quotes = soup.find_all('div', class_='quote')
    
    # Afficher les citations trouvées
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        print(text)
else:
    print("Erreur lors de la récupération de la page.")
