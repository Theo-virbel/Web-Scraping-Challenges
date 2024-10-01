import requests  # Importation de la bibliothèque pour faire des requêtes HTTP
from bs4 import BeautifulSoup  # Importation de BeautifulSoup pour l'analyse du HTML
from urllib.parse import urljoin  # Importation de urljoin pour construire des URLs complètes

# URL de la première page
url = 'https://quotes.toscrape.com/'  # Définition de la variable URL pour commencer le scraping

# Fonction pour obtenir le nombre de pages
def get_number_of_pages(url):
    current_page = url  # Initialisation de current_page avec l'URL de départ
    total_pages = 0  # Compteur pour le nombre total de pages

    while current_page:  # Boucle tant qu'il y a une page à scraper
        response = requests.get(current_page)  # Faire une requête GET sur la page actuelle
        soup = BeautifulSoup(response.text, 'html.parser')  # Analyser le contenu HTML de la page

        total_pages += 1  # Incrémenter le compteur pour chaque page visitée

        # Trouver la balise "next" pour vérifier s'il y a une page suivante
        next_button = soup.find('li', class_='next')  # Chercher l'élément suivant dans la pagination
        if next_button:  # Si un bouton "next" est trouvé
            next_link = next_button.find('a')['href']  # Obtenir le lien vers la prochaine page
            current_page = urljoin(url, next_link)  # Construire l'URL complète de la prochaine page
        else:
            current_page = None  # Aucune page suivante, terminer la boucle

    return total_pages  # Retourner le nombre total de pages

# Afficher le nombre total de pages
total_pages = get_number_of_pages(url)  # Appeler la fonction pour compter les pages
print(f'Nombre total de pages : {total_pages}')  # Afficher le résultat
