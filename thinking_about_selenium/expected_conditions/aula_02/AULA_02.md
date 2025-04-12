# Aula 2: Interações com Elementos Dinâmicos e element_to_be_clickable

## Apresentação do Tema

Por Que Usar element_to_be_clickable?
* Problema: Elementos podem estar presentes no DOM mas não clicáveis (ex.: overlays, animações).
* Solução: EC.element_to_be_clickable garante que o elemento está visível e habilitado.

## Exemplo Básico

``` python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

# Espera até que o botão "More info..." esteja clicável
botao = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "More information..."))
)
botao.click()  # Interage com o elemento
print("Pós-clique:", driver.title)
driver.quit()
```

## Desafio

* Acesse https://github.com.
* Use EC.element_to_be_clickable para aguardar o botão "Sign up" (seletor: By.CSS_SELECTOR, "[href='/signup']").
* Clique nele e imprima o título da nova página (driver.title).

## Dica:

* O botão está no canto superior direito.
* Use print(driver.current_url) para verificar se a navegação funcionou.