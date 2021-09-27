"""
Program: Automate Liking profiles in Tinder
Author: Subhashish Dhar
Date: 23/09/2021
"""

from selenium import webdriver

CHROME_DRIVER_PATH = "C:\\Development\\chromedriver"
WEB_URL = "https://tinder.com/app/recs"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(WEB_URL)

# Navigate to the login page
try:
    login = driver.find_element_by_xpath('//*[@id="s-2061886532"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
    login.click()
except:
    dismiss = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[2]/button/svg')
    dismiss.click()
    login = driver.find_element_by_xpath('//*[@id="s-2061886532"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
    login.click()
finally:
    driver.implicitly_wait(3)

# Choose login with Facebook
try:
    login_with_facebook = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    login_with_facebook.click()
except:
    more_options = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    more_options.click()
    driver.implicitly_wait(2)
    login_with_facebook = driver.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    login_with_facebook.click()
finally:
    driver.implicitly_wait(5)

# Switch windows
for window in driver.window_handles:
    print(driver.title)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to_window(fb_login_window)
driver.implicitly_wait(2)
print(driver.title)

# Provide Facebook credentials
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys("")
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys("")
login = driver.find_element_by_xpath('//*[@id="u_0_0_Sr"]')
login.click()
