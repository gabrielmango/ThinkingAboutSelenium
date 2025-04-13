from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://example.com')

# Espera e muda para um iframe com ID "frame1"
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, 'frame1'))
)

# Agora pode interagir com elementos dentro do iframe
print('Dentro do iframe!')

# Volta para o contexto principal
driver.switch_to.default_content()
