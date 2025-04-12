from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServicoChrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

opcoes = webdriver.ChromeOptions()
servico = ServicoChrome(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=opcoes)
driver.implicitly_wait(5)

url = 'https://www.python.org/'
driver.get(url)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'id-search-field'))
    )
    print(element.get_attribute('placeholder'))
except Exception as e:
    print(f'Erro: {e}')
finally:
    driver.quit()
