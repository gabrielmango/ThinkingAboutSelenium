from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServicoChrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

opcoes = webdriver.ChromeOptions()
servico = ServicoChrome(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=opcoes)

url = 'https://www.python.org/'
driver.get(url)

xpath_versao_python = '//*[@id="content"]/div/section/div[2]/div[2]/p[2]/a'

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, xpath_versao_python))
)

print(f'Versão mais recente do {element.text} em {datetime.now()}')

sleep(5)

driver.quit()
