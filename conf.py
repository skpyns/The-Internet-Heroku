# First selenium project to gather list of people from https://members.cpo.on.ca/
# Information gathered in this project is for educational purposes only

from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC

FIRST_NAME = []
LAST_NAME = []

# names = //table//td[1]/a
# nextpagebtn = class next_page

driver = webdriver.Chrome(r'C:\Users\Jelena\Desktop\python\chromedriver.exe')
driver.maximize_window()

driver.get('https://members.cpo.on.ca/public_register/create?first_name=&last_name=&city=&postal=&certificate%5B%5D=55&practice%5B%5D=5&practice%5B%5D=775&practice%5B%5D=6&practice%5B%5D=10&practice%5B%5D=13&practice%5B%5D=14&population%5B%5D=15&population%5B%5D=16&population%5B%5D=17&population%5B%5D=18&population%5B%5D=19&population%5B%5D=20&population%5B%5D=21')
current_page = int(driver.find_element_by_class_name('current').text)
# names = driver.find_elements_by_xpath('//table//td[1]/a')

while current_page <= 139:
    names = driver.find_elements_by_xpath('//table//td[1]/a')
    for name in names:
        name = name.text.split('(')[0].split(',')
        last_name = name[0]
        first_name = ''.join(name[1:]).strip()
        print(first_name, last_name)
        FIRST_NAME.append(first_name)
        LAST_NAME.append(last_name)
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'next_page')))
    element.click()
    current_page += 1
    print(current_page)

driver.close()

df = pd.DataFrame(data={'First name': FIRST_NAME, 'Last name': LAST_NAME})
df.to_csv('./project1.csv', sep=',', index=False)
