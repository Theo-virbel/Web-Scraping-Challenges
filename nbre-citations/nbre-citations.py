from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurer le WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL de la page à scraper
url = 'https://quotes.toscrape.com/scroll'
driver.get(url)

# Initialiser les variables
has_next_page = True
quotes = []

# Boucle pour scroller et charger les citations
while has_next_page:
    # Faire défiler vers le bas de la page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Attendre le chargement des nouvelles citations
    time.sleep(2)  # Ajustez si nécessaire

    # Trouver toutes les citations sur la page
    new_quotes = driver.find_elements(By.CLASS_NAME, 'quote')
    
    # Éviter les doublons
    quotes.extend([quote.text for quote in new_quotes if quote.text not in quotes])

    # Vérifier s'il y a plus de pages
    try:
        loading_element = driver.find_element(By.CLASS_NAME, 'loading')
        has_next_page = loading_element.is_displayed()  # Vérifiez l'état de l'élément de chargement
    except:
        has_next_page = False  # Si l'élément de chargement n'est pas trouvé, sortez de la boucle

# Compter le nombre total de citations
number_of_quotes = len(quotes)

# Afficher le nombre de citations
print(f"Nombre de citations: {number_of_quotes}")

# Fermer le navigateur
driver.quit()
