from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://example.com')

# Salva a janela atual
main_window = driver.current_window_handle

# Clica em um link que abre nova aba
driver.find_element(By.LINK_TEXT, 'Abrir Nova Janela').click()

# Espera a nova janela e alterna para ela
WebDriverWait(driver, 10).until(EC.new_window_is_opened(driver.window_handles))
new_window = [w for w in driver.window_handles if w != main_window][0]
driver.switch_to.window(new_window)

print('Nova aba:', driver.title)
