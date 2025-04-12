from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service as ServicoChrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

opcoes = webdriver.ChromeOptions()
servico = ServicoChrome(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=opcoes)

url = 'https://www.python.org'

downloads_locator = (By.ID, 'downloads')

try:
    driver.get(url)

    menu_downloads = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(downloads_locator, 'Downloads')
    )
    print('Menu encontrado!')

except (TimeoutException, NoSuchElementException) as e:
    print(f'Falha ao encontrar o menu: {e}')
finally:
    driver.quit()
