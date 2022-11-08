"""
importação das bibliotecas para o projeto. quando a biblioteca não exiiste utiliza:
from+nome da biblioteca import e o obejto da bilbioteca que iremos usar
quando a bilioteca ja tem:
import+nome da biblioteca
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#importação de biblioteca XLRD para trabalhar com planilhas dentro do excel
import xlrd
import time

print('Iniciando o programa.... \n')

#para abrir o areuivo em Excel 
workbook = xlrd.open_workbook(r'C:\Users\soare\Documents\Estudos\Python\projectCourse\projeto1\dominios.xls') 
#especificando a aba no Excel
sheet = workbook.sheet_by_name('Plan1')
rows = sheet.nrows
cols = sheet.ncols

#linhas para que o python não deixe "lixo" no prompt do shell
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
#dominio = ['roboscompython.com.br', 'uol.com.br', 'facebook.com.br', 'josedascouves.com.br', 'pyschool.com.br']
#for resultado in dominio:
#contagem de linhas a partir da zero
for curr_row in range(0, rows):
#contagem de celulas começando da linha zero     
    cont = sheet.cell_value(curr_row, 0)
    pesquisa = driver.find_element(By.ID, 'is-avail-field')
    time.sleep(1)
    pesquisa.clear()
    time.sleep(1)
    #pesquisa.send_keys(dominio)
    pesquisa.send_keys(cont)
    time.sleep(1)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(1)
    #time.sleep(3)
    driver.find_elements(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    time.sleep(1)
    #print('O dominio %s %s' %(dominio, driver.find_elements(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong').text))
    print('O dominio %s %s' %(cont, driver.find_elements(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')))

#time.sleep(8)
driver.close()