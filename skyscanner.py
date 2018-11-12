from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import getpass
import time

# RUBBISH #
# ------- #
# Looks like skyscanner gives an error message
# when chrome is being run by a web driver so
# this won't work


options = webdriver.ChromeOptions()
# options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get('https://skyscanner.net')

def find_id(id_name):
    return driver.find_element_by_id(id_name)

def find_class(class_name):
    return driver.find_element_by_class_name(class_name)

try:
    origin = find_id('origin-fsc-search')
    origin.click()
    origin.send_keys( 'Cardiff')

    dest = find_id('destination-fsc-search')
    dest.click()
    dest.send_keys('Everywhere')

    depart = find_id('depart-fsc-datepicker-button')
    depart.click()
    
    month = find_class('fsc-datepicker__tab-11bkT')
    month.click()
    # depart = find_class('fsc-datepicker__wholeyear-2bBIy')
    # depart.click()


finally:
    time.sleep(3)
    # driver.close()




# # click autosuggest for origin
# find_click('react-autowhatever-origin-fsc-search--item-0')
# # enter destination
# find_send_keys('destination-fsc-search', )
# # click autosuggest
# find_click('react-autowhatever-destination-fsc-search--item-0')
# # open depart datepicker
# find_click('depart-fsc-datepicker-input')

