from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://example.com')

# Espera até que o botão "More info..." esteja clicável
botao = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, 'More information...'))
)
botao.click()  # Interage com o elemento
print('Pós-clique:', driver.title)
driver.quit()
