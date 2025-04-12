from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://example.com')

# Suponha que um loader com ID "loading" desaparece após 3 segundos
try:
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, 'loading'))
    )
    print('Loader desapareceu! Página pronta.')

except TimeoutException:
    print('Loader não desapareceu no tempo esperado.')
