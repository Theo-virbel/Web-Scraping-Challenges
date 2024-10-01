from selenium import webdriver  # Importer le module pour contrôler le navigateur
from selenium.webdriver.common.by import By  # Importer les méthodes de recherche d'éléments
import json  # Importer le module pour manipuler des données JSON
import re  # Importer le module pour utiliser des expressions régulières
import time  # Importer le module pour ajouter des pauses

# Initialiser le navigateur
driver = webdriver.Chrome()  # Ouvre une fenêtre du navigateur Chrome

# Ouvrir la page avec les citations
driver.get("https://quotes.toscrape.com/js/page/10/")  # Charge l'URL spécifiée

# Attendre que la page se charge complètement
time.sleep(2)  # Pause de 2 secondes pour laisser le temps à la page de se charger

# Trouver tous les scripts sur la page
scripts = driver.find_elements(By.TAG_NAME, "script")  # Récupère tous les éléments <script>

# Chercher les données dans les scripts
json_data = None  # Variable pour stocker les données JSON
for script in scripts:  # Parcourt chaque élément script
    script_content = script.get_attribute("innerHTML")  # Obtient le contenu du script
    # Utiliser une expression régulière pour trouver les données JSON
    match = re.search(r'var data = (\[.*?\]);', script_content, re.DOTALL)
    if match:  # Si une correspondance est trouvée
        json_data = match.group(1)  # Stocker les données JSON
        break  # Sortir de la boucle après avoir trouvé les données

if json_data:  # Si les données JSON ont été trouvées
    quotes = json.loads(json_data)  # Convertir le JSON en objet Python
    first_quote = quotes[0]['text']  # Extraire le texte de la première citation
    first_author = quotes[0]['author']['name']  # Extraire le nom de l'auteur de la première citation
    print(f'Citation: {first_quote} - {first_author}')  # Afficher la citation et l'auteur
else:  # Si aucune donnée JSON n'a été trouvée
    print("Aucune donnée JSON trouvée.")  # Afficher un message d'erreur

# Fermer le navigateur
driver.quit()  # Ferme la fenêtre du navigateur
