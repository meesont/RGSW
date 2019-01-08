import time as t
from selenium import webdriver
from selenium.webdriver.common import action_chains, keys

#
driver = webdriver.Chrome('/Users/thomas/Documents/School Coding - Github/RGSW/Python/chromedriver')  # Optional argument, if not specified will search path.

driver.get('https://webmail.rgsw.org.uk/owa')

action = action_chains.ActionChains(driver)

action.send_keys(keys.Keys.COMMAND+keys.Keys.ALT+'i')
action.perform()
t.sleep(3)

action.send_keys(keys.Keys.ENTER)

action.send_keys("document.querySelectorAll('')")

user = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

user.clear()#Clears both boxes before filling
password.clear()

user.send_keys("meesont")
password.send_keys("")

driver.find_element_by_type('submit').click()
# driver.find_element_by_xpath("//input[@type='submit']").click()
