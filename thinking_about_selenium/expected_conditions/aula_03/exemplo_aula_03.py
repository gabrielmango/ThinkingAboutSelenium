from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://example.com')

# Caso 1: Elemento oculto no DOM (style="display:none")
elemento_oculto = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'elemento-oculto'))
)
print('Elemento no DOM:', elemento_oculto.get_attribute('class'))  # Funciona!

# Caso 2: Elemento visível
titulo_visivel = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.TAG_NAME, 'h1'))
)
print(
    'Texto visível:', titulo_visivel.text
)  # Só funciona se o elemento estiver visível!
