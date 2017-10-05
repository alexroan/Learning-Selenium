from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://tripsi.io')
assert "Tripsi" in driver.title
# Enter search airport
leave_from_input = driver.find_element_by_id('leaveFrom')
leave_from_input.clear()
leave_from_input.send_keys('Cardiff')
# Select currency
currency_select = Select(driver.find_element_by_id('currencySelect'))
currency_select.select_by_value('EUR')
# Click go
search_button = driver.find_element_by_id('searchbutton')
search_button.click()
driver.close()