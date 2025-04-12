from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://example.com')

# Espera até que o texto "Example" apareça no <h1>
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), 'Example Domain')
)
print('Texto encontrado!')
