# 🚀 Aula 3: visibility_of_element_located vs presence_of_element_located

## Apresentação do Tema

Entender a diferença crítica entre:
* presence_of_element_located: Verifica se o elemento existe no DOM (mesmo que invisível).
* visibility_of_element_located: Verifica se o elemento está visível na tela (não oculto por CSS, com tamanho > 0).

## Exemplo Básico

``` python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

# Caso 1: Elemento oculto no DOM (style="display:none")
elemento_oculto = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "elemento-oculto"))
)
print("Elemento no DOM:", elemento_oculto.get_attribute("class"))  # Funciona!

# Caso 2: Elemento visível
titulo_visivel = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.TAG_NAME, "h1"))
)
print("Texto visível:", titulo_visivel.text)  # Só funciona se o elemento estiver visível!
```

## Desafio

* Acesse https://www.selenium.dev/documentation/.
* Use EC.visibility_of_element_located para aguardar o título principal.
* Use EC.presence_of_element_located para buscar o elemento `<footer>` (normalmente oculto até rolar a página).
* Imprima: Texto do título visível. Atributo class do `<footer>`

## Dica:

* Use By.TAG_NAME para o footer e By.CSS_SELECTOR para o título.
