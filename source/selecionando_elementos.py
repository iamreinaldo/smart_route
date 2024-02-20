from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.ibge.gov.br")
barra_busca = driver.find_element(By.ID, "mod-search-searchword")
barra_busca.send_keys("Inflação")