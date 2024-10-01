from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurer le driver (par exemple, Chrome)
driver = webdriver.Chrome()  # Assure-toi d'avoir installé le driver pour le navigateur que tu utilises

# Ouvrir la page
driver.get('https://quotes.toscrape.com/scroll')

# Attendre que la page se charge correctement
time.sleep(2)

# Initialiser des variables
all_quotes = set()
has_next_page = True

# Fonction pour scroller et récupérer les citations
while has_next_page:
    # Extraire les citations actuelles
    quotes = driver.find_elements(By.CSS_SELECTOR, ".quote .text")
    
    # Ajouter les citations à l'ensemble (pour éviter les doublons)
    for quote in quotes:
        all_quotes.add(quote.text)

    # Scroller vers le bas pour charger plus de citations
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Attendre le chargement de la nouvelle page
    time.sleep(2)
    
    # Vérifier si des nouvelles citations ont été ajoutées (si non, fin du défilement)
    new_quotes = driver.find_elements(By.CSS_SELECTOR, ".quote .text")
    if len(new_quotes) == len(quotes):
        has_next_page = False

# Afficher le nombre total de citations trouvées
print(f"Nombre total de citations : {len(all_quotes)}")

# Fermer le navigateur
driver.quit()
