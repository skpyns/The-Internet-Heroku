# Find and download exchange rates from NBS https://nbs.rs/sr_RS/indeks/

from selenium import webdriver
from driver_location import path
import pandas as pd
import time

filename = time.strftime("%Y%m%d")

CURRENCY_NAME = []
COUNTRY_NAME = []
VALID_FOR = []
EXCHANGE_RATE = []

driver = webdriver.Chrome(path)
driver.maximize_window()

driver.get('https://nbs.rs/sr_RS/indeks/')
driver.find_element_by_link_text('Курсна листа НБС').click()
time.sleep(1)
driver.find_elements_by_xpath('//*[@id="panelBodyFive"]//h6/a')[0].click()

iframe = driver.find_element_by_id('frameId')
driver.switch_to.frame(iframe)
table_location = driver.find_element_by_id('index:srednjiKursLista')

table = table_location.find_element_by_tag_name('tbody')

max_rows = table.find_elements_by_tag_name('tr')
for row in max_rows:
    data = row.text.split()
    if len(data) == 5:
        currency_name = data[0]
        country_name = data[2]
        valid_for = data[3]
        exchange_rate = data[4]
    elif len(data) == 6:
        currency_name = data[0]
        country_name = data[2] + ' ' + data[3]
        valid_for = data[4]
        exchange_rate = data[5]
    else:
        currency_name = data[0]
        country_name = data[2] + ' ' + data[3] + ' ' + data[4]
        valid_for = data[5]
        exchange_rate = data[6]
    CURRENCY_NAME.append(currency_name)
    COUNTRY_NAME.append(country_name)
    VALID_FOR.append(valid_for)
    EXCHANGE_RATE.append(exchange_rate)

driver.quit()
time.sleep(3)

df = pd.DataFrame(data={'Currency name': CURRENCY_NAME, 'Country Name': COUNTRY_NAME, 'Valid for': VALID_FOR, 'Exchange Rate': EXCHANGE_RATE})
print(df)
df.to_csv('./NBSproject' + filename +'.csv', sep=',', index=False)