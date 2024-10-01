import requests
from bs4 import BeautifulSoup

# URL de base pour accéder aux catégories de livres
base_url = "https://books.toscrape.com/catalogue/category/books/"

# Liste complète des catégories à scraper
categories = [
    "travel_2",
    "mystery_3",
    "historical-fiction_4",
    "sequential-art_5",
    "classics_6",
    "philosophy_7",
    "romance_8",
    "womens-fiction_9",
    "fiction_10",
    "childrens_11",
    "religion_12",
    "nonfiction_13",
    "music_14",
    "default_15",
    "science-fiction_16",
    "sports-and-games_17",
    "fantasy_19",
    "new-adult_20",
    "young-adult_21",
    "science_22",
    "poetry_23",
    "paranormal_24",
    "art_25",
    "psychology_26",
    "autobiography_27",
    "parenting_28",
    "adult-fiction_29",
    "humor_30",
    "horror_31",
    "history_32",
    "food-and-drink_33",
    "christian-fiction_34",
    "business_35",
    "biography_36",
    "thriller_37",
    "contemporary_38",
    "spirituality_39",
    "academic_40",
    "self-help_41",
    "historical_42",
    "christian_43",
    "suspense_44",
    "short-stories_45",
    "novels_46",
    "health_47",
    "politics_48",
    "cultural_49",
    "erotica_50",
    "crime_51"
]

# Dictionnaire pour stocker les résultats
results = {}

# Parcourir chaque catégorie
for category in categories:
    # Construire l'URL pour chaque catégorie
    url = base_url + category + "/index.html"
    
    # Faire une requête pour obtenir le contenu de la page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Trouver le nombre total de livres dans la catégorie
    num_books_text = soup.find("form", class_="form-horizontal").find("strong").text
    num_books = int(num_books_text)  # Convertir le texte en entier

    # Liste pour stocker les prix des livres
    prices = []

    # Trouver tous les livres sur la première page
    for book in soup.find_all("article", class_="product_pod"):
        # Récupérer le prix de chaque livre
        price_text = book.find("p", class_="price_color").text[1:]  # Enlever le symbole £
        prices.append(float(price_text))  # Ajouter le prix à la liste

    # Vérifier si une page suivante existe et la parcourir si nécessaire
    next_button = soup.find("li", class_="next")
    while next_button:
        # Construire l'URL de la page suivante
        next_page_url = next_button.find("a")["href"]
        url = base_url + category + "/" + next_page_url

        # Faire une requête pour obtenir le contenu de la page suivante
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Trouver tous les livres sur la nouvelle page
        for book in soup.find_all("article", class_="product_pod"):
            price_text = book.find("p", class_="price_color").text[1:]  # Enlever le symbole £
            prices.append(float(price_text))  # Ajouter le prix à la liste

        # Vérifier si une autre page suivante existe
        next_button = soup.find("li", class_="next")

    # Calculer le prix moyen
    avg_price = sum(prices) / len(prices) if prices else 0

    # Stocker les résultats dans le dictionnaire
    results[category] = {
        "number_of_books": num_books,
        "average_price": avg_price
    }

# Afficher les résultats
for category, data in results.items():
    print(f"Category: {category.replace('_', ' ').title()}")
    print(f"Number of books: {data['number_of_books']}")
    print(f"Average price: £{data['average_price']:.2f}")
    print("-" * 40)
