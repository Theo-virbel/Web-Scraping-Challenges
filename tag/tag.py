import requests
from bs4 import BeautifulSoup
from collections import Counter

# URL de la page à scraper
url = 'https://quotes.toscrape.com/tableful/'

# Faire la requête HTTP pour obtenir le contenu de la page
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Parser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver tous les <td> contenant les tags
    tags_td = soup.find_all('td', style='padding-bottom: 2em;')

    # Extraire tous les tags et les stocker dans une liste
    all_tags = []
    for td in tags_td:
        a_tags = td.find_all('a')
        for a in a_tags:
            all_tags.append(a.text.strip())  # Utiliser strip() pour nettoyer l'espace

    # Compter la fréquence des tags
    tag_counts = Counter(all_tags)

    # Trouver le tag le plus répétitif
    most_common_tag = tag_counts.most_common(1)

    # Afficher le tag le plus fréquent
    if most_common_tag:
        print(f"Le tag le plus répétitif est : '{most_common_tag[0][0]}' avec {most_common_tag[0][1]} occurrences.")

    # Afficher tous les tags pour chaque citation
    print("\nTags pour chaque citation :")
    for td in tags_td:
        tags = [a.text.strip() for a in td.find_all('a')]
        print(tags)

else:
    print(f"Erreur lors de la requête : {response.status_code}")
