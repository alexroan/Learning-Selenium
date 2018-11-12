from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import getpass

driver = webdriver.Chrome()
driver.get('https://twitter.com/login')

# Get username and password
username = input('Twitter username:')
password = getpass.getpass('Password:')

# Enter username
username_input = driver.find_element_by_class_name('js-username-field')
username_input.clear()
username_input.send_keys(username)

# Enter password
password_input = driver.find_element_by_class_name("js-password-field")
password_input.clear()
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

# Wait and close the driver
ui.WebDriverWait(driver, 25)
driver.close()