from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import getpass

driver = webdriver.Chrome()
driver.get('https://twitter.com')

open_dialog_btn = driver.find_element_by_class_name('js-login')
open_dialog_btn.click()

username = input('Twitter username:')
username_input = driver.find_element_by_class_name('js-signin-email')
username_input.send_keys(username)

password = getpass.getpass('Password:')
password_input = driver.find_element_by_xpath("//input[@type='password']")
password_input.send_keys(password)

submit_button = driver.find_element_by_class_name('js-submit')
submit_button.click()

ui.WebDriverWait(driver, 25)
driver.close()