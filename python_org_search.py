from selenium import webdriver
# Keys
from selenium.webdriver.common.keys import Keys

# Create instance of Chrome
driver = webdriver.Chrome()
# Go to a web page
driver.get("http://www.python.org")
# Assertion that the title of the page has 'Python' in it
assert "Python" in driver.title
# Many find_element_by_*() methods
# Name is one of them
elem = driver.find_element_by_name("q")
# Clear any text in the input field
elem.clear()
# Populate input
elem.send_keys("pycon")
# Enter
elem.send_keys(Keys.RETURN)
# Assert if no results are found
assert "No results found." not in driver.page_source
# Close the driver
 driver.close()