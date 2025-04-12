# 🚀 Aula 5: invisibility_of_element_located

## Apresentação do Tema

Aprender a usar EC.invisibility_of_element_located para verificar quando um elemento deixa de estar visível (útil para loaders, pop-ups, etc.).

## Exemplo Básico

``` python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

# Suponha que um loader com ID "loading" desaparece após 3 segundos
try:
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "loading"))
    )
    print("Loader desapareceu! Página pronta.")

except TimeoutException:
    print("Loader não desapareceu no tempo esperado.")
```

## Desafio

* Acesse https://the-internet.herokuapp.com/dynamic_loading/1.
* Clique no botão "Start".
* Use EC.invisibility_of_element_located para aguardar o desaparecimento do loader (ID: "loading").
* Verifique se o texto "Hello World!" aparece (ID: "finish").

## Dica:

* O loader tem ID loading e o texto final tem ID finish.
