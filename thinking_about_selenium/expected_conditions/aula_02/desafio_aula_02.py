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

url = 'https://github.com/'
driver.get(url)

signup_locator = (
    By.XPATH,
    '/html/body/div[1]/div[3]/header/div/div[2]/div/div/a',
)

try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(signup_locator)
    ).click()

    if url != driver.current_url:
        print(f'Título da nova página: {driver.title}')

except Exception as e:
    print(f'Erro: {e}')
except (TimeoutException, NoSuchElementException) as e:
    print(f'Erro durante a execução: {e}')
finally:
    driver.quit()
