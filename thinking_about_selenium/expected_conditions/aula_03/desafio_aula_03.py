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

url = 'https://www.selenium.dev/documentation/'

title_locator = (By.CSS_SELECTOR, 'h1')
footer_locator = (By.TAG_NAME, 'footer')

try:
    driver.get(url)

    visible_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(title_locator)
    )
    print('Título visível:', visible_title.text)

    footer = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(footer_locator)
    )
    print('Classe do footer:', footer.get_attribute('class'))

except (TimeoutException, NoSuchElementException) as e:
    print(f'Erro durante a execução: {e}')
finally:
    driver.quit()
