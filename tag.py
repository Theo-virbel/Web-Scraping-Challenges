import requests
from bs4 import BeautifulSoup
from collections import Counter

# URL de la page à scrapper
url = 'https://quotes.toscrape.com/tableful/'

# Effectuer une requête GET pour récupérer le contenu de la page
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Trouver la section contenant les tags
    tags_section = soup.find('td', rowspan='5')
    
    if tags_section:
        # Trouver tous les tags dans cette section
        tags = tags_section.find_all('a')
    
        # Extraire le texte de chaque tag et les compter
        tag_list = [tag.text for tag in tags]
        tag_counts = Counter(tag_list)

        # Trouver le tag le plus répétitif
        most_common_tag = tag_counts.most_common(1)

        # Afficher le tag le plus fréquent sans le nombre d'occurrences
        if most_common_tag:
            print(f"Le tag le plus répétitif est '{most_common_tag[0][0]}'.")
        else:
            print("Aucun tag trouvé.")
    else:
        print("Aucune section de tags trouvée.")
else:
    print(f"Erreur lors de la récupération de la page : {response.status_code}")
