from driverfile import driver
import requests

broken_imgs = 0
driver.get('http://the-internet.herokuapp.com/broken_images')
example = driver.find_element_by_class_name('example')
images = example.find_elements_by_tag_name('img')
for image in images:
    r = requests.get(image.get_attribute('src'))
    if r.status_code != 200:
        broken_imgs += 1
    else:
        print('Image working just fine')

print('This webpage has total ' + str(broken_imgs) + ' of broken images.')

driver.quit()