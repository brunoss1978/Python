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

"""
variavel com o nome de driver
observação: estava dando erro na sintaxe da linha de codigo abaixo. o professor Diogo disse para caolocar um 'r' antes da string
"""
driver = webdriver.Chrome(r'C:\Users\soare\Documents\Estudos\Python\chromedriver.exe', options=options)
driver.get('https://registro.br/')

"""
a sintaxe correta para ID e a:
pesquisa = driver.find_element(By.ID, 'is-avail-field') e não:
pesquisa = driver.find_element_by_ID('is-avail-field')
"""

dominio = ['roboscompython.com.br', 'uol.com.br', 'facebook.com.br', 'josedascouves.com.br', 'pyschool.com.br']
for resultado in dominio:
    pesquisa = driver.find_element(By.ID, 'is-avail-field')
    pesquisa.clear()
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.find_elements(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    print('O dominio %s %s' %(dominio, driver.find_elements(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong').text))


#time.sleep(8)
driver.close()