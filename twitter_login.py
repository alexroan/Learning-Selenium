from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import getpass

driver = webdriver.Chrome()
driver.get('https://twitter.com')

# Open the login dialog
open_dialog_btn = driver.find_element_by_class_name('js-login')
open_dialog_btn.click()

# Get and enter username
username = input('Twitter username:')
username_input = driver.find_element_by_class_name('js-signin-email')
username_input.send_keys(username)

# Get and enter password
password = getpass.getpass('Password:')
password_input = driver.find_element_by_xpath("//input[@type='password']")
password_input.send_keys(password)

# Click login
submit_button = driver.find_element_by_class_name('js-submit')
submit_button.click()

# Wait and close the driver
ui.WebDriverWait(driver, 25)
driver.close()