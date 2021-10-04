"""
Program: Searches a User and follows their followers
Author: Subhashish Dhar
Date: 30/09/2021
"""

import os
import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "C:\\Development\\chromedriver"
INSTA_URL = "https://www.instagram.com/accounts/login/?source=auth_switcher"
INSTA_EMAIL = "subbu.pybot@gmail.com"
INSTA_PASSWORD = os.environ.get("INSTA_PASSWORD")
SIMILAR_ACCOUNT = "python.coder_"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

# Log in
driver.get(INSTA_URL)
driver.implicitly_wait(5)
username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys(INSTA_EMAIL)
password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys(INSTA_PASSWORD)
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
login.click()
driver.implicitly_wait(5)

# Take care of the pop ups
save_login_not_now = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
save_login_not_now.click()
driver.implicitly_wait(5)
notif_not_now = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
notif_not_now.click()
driver.implicitly_wait(5)

# Find the account and their followers
driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
driver.implicitly_wait(3)
followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
followers.click()
driver.implicitly_wait(5)

# Follow people
popup = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/ul/div/li[1]/div/div[3]/button')
for i in range(30):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
all_buttons = driver.find_elements_by_css_selector("li button")
for button in all_buttons:
    try:
        button.click()
        time.sleep(2)
    except ElementClickInterceptedException:
        cancel_button = driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
        cancel_button.click()
        driver.implicitly_wait(2)
