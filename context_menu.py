import time

from driverfile import driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

driver.get('http://the-internet.herokuapp.com/context_menu')
action = ActionChains(driver)
alert = Alert(driver)
element = driver.find_element_by_id('hot-spot')
action.context_click(element).perform()
print(alert.text)
alert.accept()

time.sleep(2)
driver.quit()
