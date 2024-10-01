from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuration du driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Ouvre la page du formulaire
url = 'https://quotes.toscrape.com/search.aspx'
driver.get(url)

# Sélectionner Albert Einstein dans le menu déroulant de l'auteur
author_select = Select(driver.find_element(By.ID, "author"))
author_select.select_by_visible_text("Albert Einstein")

# Sélectionner 'music' dans le menu déroulant de la balise
tag_select = Select(driver.find_element(By.ID, "tag"))
tag_select.select_by_visible_text("music")

# Cliquer sur le bouton de recherche
search_button = driver.find_element(By.XPATH, '//input[@value="Search"]')
search_button.click()

# Pause pour s'assurer que la page est chargée
time.sleep(2)

# Extraire la citation
quote = driver.find_element(By.CLASS_NAME, "content").text

# Affiche la citation trouvée
print("Citation trouvée:", quote)

# Ferme le driver
driver.quit()
