from selenium import webdriver
import time

path = r'C:\Users\Jelena\Desktop\python\geckodriver.exe'
driver = webdriver.Firefox(executable_path=path)

driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
addelement = driver.find_element_by_xpath('//*[@id="content"]/div/button')


for i in range(1, 11):
    addelement.click()

time.sleep(2)

removeelements = driver.find_elements_by_xpath('//*[@id="content"]/div/div/button')
for elem in removeelements:
    elem.click()

time.sleep(5)

driver.quit()