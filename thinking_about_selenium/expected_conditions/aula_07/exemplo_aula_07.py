from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://example.com/alert-page')

try:
    # Espera pelo alerta e aceita
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print('Texto do alerta:', alert.text)
    alert.accept()  # Clica em "OK"

except TimeoutException:
    print('Alerta não apareceu')
