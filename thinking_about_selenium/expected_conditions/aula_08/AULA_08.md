# 🚀 Aula 8: new_window_is_opened (Controle de Janelas/Aba)

## Apresentação do Tema

Aprender a verificar quando uma nova janela/aba é aberta e como alternar entre elas.

## Quando usar?

* Quando ações como clicar em links/buttons abrem novas abas.
* Para testar sistemas com redirecionamentos complexos.

## Exemplo Básico

``` python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

# Salva a janela atual
main_window = driver.current_window_handle

# Clica em um link que abre nova aba
driver.find_element(By.LINK_TEXT, "Abrir Nova Janela").click()

# Espera a nova janela e alterna para ela
WebDriverWait(driver, 10).until(EC.new_window_is_opened(driver.window_handles))
new_window = [w for w in driver.window_handles if w != main_window][0]
driver.switch_to.window(new_window)

print("Nova aba:", driver.title)
```

## Desafio

* Acesse https://the-internet.herokuapp.com/windows.
* Clique no link "Click Here" (abre nova janela).
* Use EC.new_window_is_opened para verificar a nova janela.
* Alterne para ela e imprima o texto "New Window".
* Volte para a janela original e imprima "Opening a new window".

## Dica:

* Use driver.window_handles para gerenciar as janelas.
