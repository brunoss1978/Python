"""
importação das bibliotecas para o projeto. quando a biblioteca não exiiste utiliza:
from+nome da biblioteca import e o obejto da bilbioteca que iremos usar
quando a bilioteca ja tem:
import+nome da biblioteca
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--disable-logging')
options.add_argument('--log-level=3')

#variavel com o nome de driver
driver = webdriver.Chrome(r'C:\Users\soare\Documents\Estudos\Python\chromedriver.exe', options=options)
driver.get('https://registro.br/')

pesquisa = driver.find_element(By.ID, 'is-avail-field')
pesquisa.clear()
dominio = 'roboscompython.com.br'
pesquisa.send_keys(dominio)
pesquisa.send_keys(Keys.RETURN)
time.sleep(3)

driver.find_elements(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')
print('O dominio %s %s' %(dominio, driver.find_elements(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')))


time.sleep(8)
driver.close()