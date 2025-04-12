# 🚀 Aula 4: text_to_be_present_in_element

## Apresentação do Tema

Aprender a usar EC.text_to_be_present_in_element para verificar se um texto específico aparece em um elemento.

## Exemplo Básico

``` python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

# Espera até que o texto "Example" apareça no <h1>
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Example Domain")
)
print("Texto encontrado!")
```

## Desafio

* Acesse https://www.python.org.
* Use EC.text_to_be_present_in_element para verificar se o texto "Downloads" está no menu principal.
* Imprima "Menu encontrado!" se o texto existir.

## Dica:

* Inspecione o menu para encontrar o locator correto (sugestão: use By.ID, "downloads").
