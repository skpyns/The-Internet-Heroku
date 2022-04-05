import time

from driverfile import driver

driver.get('http://the-internet.herokuapp.com/checkboxes')

checkboxes = driver.find_elements_by_css_selector("input[type='checkbox']")
time.sleep(2)
for checkbox in checkboxes:
    if checkbox.is_selected():
        pass
    else:
        checkbox.click()

time.sleep(5)
driver.quit()