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

url = 'https://the-internet.herokuapp.com/dynamic_loading/1'

start_locator = (By.XPATH, '//*[@id="start"]/button')
loading_locator = (By.ID, 'loading')
finish_locator = (By.ID, 'finish')

try:
    driver.get(url)

    print('Clicando no botão Start...')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(start_locator)
    ).click()

    print('Aguardando loader desaparecer...')
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located(loading_locator)
    )

    print('Verificando texto final...')
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(finish_locator, 'Hello World!')
    )
    print('Sucesso! Texto encontrado.')

except (TimeoutException, NoSuchElementException) as e:
    print(f'Falha no processo: {e}')

finally:
    driver.quit()
