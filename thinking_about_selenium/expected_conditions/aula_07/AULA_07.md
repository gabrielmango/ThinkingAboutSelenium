# 🚀 Aula 7: alert_is_present (Trabalhando com Alertas JavaScript)

## Apresentação do Tema

Aprender a manipular alertas, confirmações e prompts do JavaScript usando EC.alert_is_present.

## Quando usar?

* Quando o sistema exibe pop-ups de:
    * Alerta (OK)
    * Confirmação (OK/Cancelar)
    * Prompt (Input + OK/Cancelar)

* Exemplo: Aceitar termos, lidar com erros, ou preencher diálogos.

## Exemplo Básico

``` python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com/alert-page")

try:
    # Espera pelo alerta e aceita
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Texto do alerta:", alert.text)
    alert.accept()  # Clica em "OK"

except TimeoutException:
    print("Alerta não apareceu")
```

## Desafio

* Acesse https://the-internet.herokuapp.com/javascript_alerts.
* Clique no botão "Click for JS Alert".
* Use EC.alert_is_present para capturar o alerta e imprimir seu texto.
* Aceite o alerta e verifique se o texto "You successfully clicked an alert" aparece na página.

## Dica:

* O resultado aparece em um elemento com ID "result".
