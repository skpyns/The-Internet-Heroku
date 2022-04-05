from selenium import webdriver
import time

path = r'C:\Users\Jelena\Desktop\python\geckodriver.exe'
driver = webdriver.Firefox(executable_path=path)

driver.get('http://the-internet.herokuapp.com/challenging_dom')

content = driver.find_element_by_id('content')
button1 = content.find_elements_by_css_selector('.button')[1]
button2 = content.find_element_by_css_selector('.alert')
button3 = content.find_element_by_css_selector('.success')

canvas = content.find_element_by_id('canvas')

edit_buttons = content.find_elements_by_link_text('edit')
delete_buttons = content.find_elements_by_link_text('delete')

print(button1.text)
print(button2.text)
print(button3.text)

print(len(edit_buttons))
print(len(delete_buttons))

# print(content.text)

driver.quit()