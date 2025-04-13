# 🚀 Aula 6: frame_to_be_available_and_switch_to_it

## Apresentação do Tema

Aprender a usar EC.frame_to_be_available_and_switch_to_it para interagir com elementos dentro de iframes.

## Exemplo Básico

``` python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

# Espera e muda para um iframe com ID "frame1"
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1"))
)

# Agora pode interagir com elementos dentro do iframe
print("Dentro do iframe!")

# Volta para o contexto principal
driver.switch_to.default_content()
```

## Desafio

* Acesse https://the-internet.herokuapp.com/iframe.
* Use EC.frame_to_be_available_and_switch_to_it para mudar para o iframe.
* Localize o elemento `<p>` editável e insira o texto "Teste com Selenium!".
* Volte para o contexto principal e clique no link "Elemental Selenium".

## Dica:

* O iframe tem ID "mce_0_ifr".
* O elemento editável tem ID "tinymce".
* Use driver.switch_to.default_content() para voltar ao contexto principal.
