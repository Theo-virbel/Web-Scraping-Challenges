import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL du site principal
base_url = 'http://books.toscrape.com/'

# Fonction pour scraper une catégorie avec gestion de la pagination
def scrape_category(category_url):
    total_books = 0
    total_price = 0.0
    current_page_number = 1
    
    while True:
        # Construire l'URL de la page actuelle
        current_page_url = f"{category_url}/page-{current_page_number}.html"
        response = requests.get(current_page_url)
        
        # Vérifier si la requête est réussie
        if response.status_code != 200:
            break  # Si la page n'existe pas, sortir de la boucle
        
        soup = BeautifulSoup(response.content, 'html.parser')

        # Trouver tous les livres sur la page
        books = soup.find_all('article', class_='product_pod')

        # Si aucun livre n'est trouvé, sortir de la boucle
        if not books:
            break

        # Parcourir chaque livre pour extraire le prix
        for book in books:
            # Trouver le prix dans l'élément 'p' avec la classe 'price_color'
            price = book.find('p', class_='price_color').text
            # Convertir le prix en flottant en enlevant le signe de la livre (£)
            price = float(price.replace('£', ''))

            # Ajouter le prix au total
            total_price += price
            # Incrémenter le compteur de livres
            total_books += 1

        # Passer à la page suivante
        current_page_number += 1

    # Retourner le nombre total de livres et le prix moyen
    if total_books > 0:
        average_price = total_price / total_books
    else:
        average_price = 0

    return total_books, average_price

# Faire une requête pour obtenir la page d'accueil
response = requests.get(base_url)

# Vérifier si la requête est réussie
if response.status_code == 200:
    # Parser la page d'accueil
    soup = BeautifulSoup(response.content, 'html.parser')

    # Trouver la section des catégories
    categories_section = soup.find('ul', class_='nav nav-list')

    # Extraire toutes les catégories
    categories = categories_section.find_all('a')

    # Parcourir chaque catégorie (sauf la première qui est "Books")
    for category in categories[1:]:
        # Nom de la catégorie
        category_name = category.text.strip()
        # URL de la catégorie
        category_url = urljoin(base_url, category['href']).replace('/index.html', '')

        # Scraper la catégorie
        total_books, average_price = scrape_category(category_url)

        # Afficher les résultats pour la catégorie
        print(f"Catégorie : {category_name}")
        print(f"Nombre de livres : {total_books}")
        print(f"Prix moyen : £{average_price:.2f}")
        print('-' * 40)

else:
    print("Échec de la requête, statut :", response.status_code)
