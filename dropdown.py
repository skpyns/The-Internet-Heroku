from driverfile import driver
from selenium.webdriver.support.ui import Select
import time

driver.get('http://the-internet.herokuapp.com/dropdown')
select = Select(driver.find_element_by_id('dropdown'))

select.select_by_index(1)
time.sleep(2)

select.select_by_index(2)
time.sleep(2)


driver.quit()