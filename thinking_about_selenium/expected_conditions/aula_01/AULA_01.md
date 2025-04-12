# Aula 1: Introdução ao expected_conditions e presence_of_element_located

## Apresentação do Tema

O selenium.webdriver.support.expected_conditions (EC) é usado para definir condições de espera explícita no Selenium, evitando falhas em testes devido a elementos não carregados ou dinâmicos.
Por que estudar? Sem EC, seus testes podem falhar aleatoriamente devido a timing issues (elementos não estarem prontos quando o Selenium tenta interagir).

## Exemplo Básico

``` python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

# Espera até que o elemento <h1> esteja presente na página
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "h1"))
)
print(element.text)
driver.quit()
```

## Desafio

* Acesse https://python.org.
* Use EC.presence_of_element_located para aguardar o carregamento da barra de busca (input com id="id-search-field").
* Imprima o atributo placeholder do input encontrado.