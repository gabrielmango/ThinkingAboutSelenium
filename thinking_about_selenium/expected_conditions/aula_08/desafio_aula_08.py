import time

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

url = 'https://the-internet.herokuapp.com/windows'

link_locator = (By.LINK_TEXT, 'Click Here')
new_window_text_locator = (By.TAG_NAME, 'h3')
main_window_text_locator = (By.TAG_NAME, 'h3')

try:
    driver.get(url)

    # Janela principal
    main_window = driver.current_window_handle
    print('Janela principal:', driver.title)

    # Abre nova janela
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(link_locator)
    ).click()

    # Espera nova janela
    WebDriverWait(driver, 10).until(
        EC.new_window_is_opened(driver.window_handles)
    )

    # Alterna para nova janela
    new_window = [w for w in driver.window_handles if w != main_window][0]
    driver.switch_to.window(new_window)

    # Verifica texto na nova janela
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(new_window_text_locator, 'New Window')
    )
    print('Nova janela:', driver.find_element(*new_window_text_locator).text)

    # Volta para janela principal
    driver.switch_to.window(main_window)

    # Verifica texto na janela principal
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            main_window_text_locator, 'Opening a new window'
        )
    )
    print(
        'Janela principal:',
        driver.find_element(*main_window_text_locator).text,
    )

except (TimeoutException, NoSuchElementException) as e:
    print(f'Falha no processo: {e}')

finally:
    driver.quit()
