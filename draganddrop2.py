from driverfile import driver
from selenium.webdriver.common.action_chains import ActionChains
import time

# path = r'C:\Users\Jelena\Desktop\python\geckodriver.exe'
# driver = webdriver.Firefox(executable_path=path)

driver.get('http://the-internet.herokuapp.com/drag_and_drop')
action = ActionChains(driver)

source = driver.find_element_by_css_selector('div#column-b.column')
target = driver.find_element_by_css_selector('div#column-a.column')

action.click_and_hold(source).perform()

driver.quit()