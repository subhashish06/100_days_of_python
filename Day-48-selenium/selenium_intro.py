"""
Program: Get the Upcoming Events in python.org website
Author: Subhashish Dhar
Date: 20/09/2021
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:\\Development\\chromedriver"
WEB_URL = "https://www.python.org/"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(WEB_URL)

dates = driver.find_elements(by=By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
dates = [date.text for date in dates]
print(dates)

events = driver.find_elements(by=By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')
events = [event.text for event in events]
print(events)

result = {}
for index, time in enumerate(dates):
    result[index] = {"time": time, "name": events[index]}
print(result)

for key, value in result.items():
    print(f"{value['time']} : {value['name']}")

driver.quit()
