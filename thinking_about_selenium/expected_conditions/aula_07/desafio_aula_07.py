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

url = 'https://the-internet.herokuapp.com/javascript_alerts'

alert_button_locator = (
    By.XPATH,
    '//button[contains(text(), "Click for JS Alert")]',
)
result_locator = (By.ID, 'result')

try:
    driver.get(url)

    print('Clicando no botão de alerta...')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(alert_button_locator)
    ).click()

    print('Aguardando alerta...')
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print('Texto do alerta:', alert.text)
    alert.accept()

    print('Verificando resultado...')
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            result_locator, 'You successfully clicked an alert'
        )
    )

    print('Teste concluído com sucesso!')

except (TimeoutException, NoSuchElementException) as e:
    print(f'Falha no processo: {e}')

finally:
    driver.quit()
