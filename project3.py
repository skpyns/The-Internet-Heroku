import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from driver_location import path

fromDate = '01.01.2022.'
toDate = '11.03.2022.'
graphname = time.strftime("%Y%m%d")

driver = webdriver.Chrome(path)
driver.maximize_window()

driver.get('https://nbs.rs/sr_RS/indeks/')
driver.find_element_by_link_text('Курсна листа НБС').click()

driver.implicitly_wait(10)
driver.find_elements_by_xpath('//*[@id="panelBodyFive"]//h6/a')[5].click()
time.sleep(5)

# switch to iframe and insert date and gather data
iframe = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframe)
start_date = driver.find_element_by_id('inputPeriod:Od')
start_date.send_keys(Keys.CONTROL, 'a')
start_date.send_keys(Keys.BACKSPACE)
start_date.send_keys(fromDate)
end_date = driver.find_element_by_id('inputPeriod:Do')
end_date.send_keys(Keys.CONTROL, 'a')
end_date.send_keys(Keys.BACKSPACE)
end_date.send_keys(toDate)
value = driver.find_element_by_id('inputPeriod:valutaInner')
value.click()
driver.find_element_by_xpath('//*[@id="inputPeriod:valutaInner"]/option[37]').click()
driver.find_element_by_id('inputPeriod:vrstaInner').click()
driver.find_element_by_xpath('//*[@id="inputPeriod:vrstaInner"]/option[3]').click()
driver.find_element_by_id('inputPeriod:buttonShow').click()
driver.switch_to.default_content()

driver.implicitly_wait(10)
iframe2 = driver.find_element_by_id('frameId')
driver.switch_to.frame(iframe2)
confirmDateFrom = driver.find_element_by_id('index:id42').text
confirmDateTo = driver.find_element_by_id('index:id44').text
with open((graphname+'.png'), 'wb') as file:
    graph = driver.find_element_by_class_name('imageResponsive')
    file.write(graph.screenshot_as_png)

driver.switch_to.default_content()
driver.quit()

assert (confirmDateFrom == fromDate) and (confirmDateTo == toDate)