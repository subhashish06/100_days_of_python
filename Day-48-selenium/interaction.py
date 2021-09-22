"""
Program: Signing Up for Practice
Author: Subhashish Dhar
Date: 21/09/2021
"""

from selenium import webdriver

CHROME_DRIVER_PATH = "C:\\Development\\chromedriver"
WEB_URL = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(WEB_URL)

f_name = driver.find_element_by_name("fName")
f_name.send_keys("Subhashish")
l_name = driver.find_element_by_name("lName")
l_name.send_keys("Dhar")
email = driver.find_element_by_name("email")
email.send_keys("subbu.pybot@gmail.com")

signup = driver.find_element_by_class_name("btn")
signup.click()

# driver.quit()
