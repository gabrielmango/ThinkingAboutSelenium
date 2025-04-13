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

url = 'https://the-internet.herokuapp.com/iframe'

iframe_locator = (By.ID, 'mce_0_ifr')
editor_locator = (By.ID, 'tinymce')
link_locator = (By.LINK_TEXT, 'Elemental Selenium')

try:
    driver.get(url)

    print('Mudando para o iframe...')
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it(iframe_locator)
    )

    print('Inserindo texto no editor...')
    editor = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(editor_locator)
    )
    editor.clear()
    editor.send_keys('Teste com Selenium!')

    print('Voltando ao contexto principal...')
    driver.switch_to.default_content()

    print('Clicando no link...')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(link_locator)
    ).click()
    print('Sucesso!')

except (TimeoutException, NoSuchElementException) as e:
    print(f'Falha no processo: {e}')

finally:
    driver.quit()
