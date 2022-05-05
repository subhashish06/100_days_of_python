"""
Program: Cookie clicker Game
Author: Subhashish Dhar
Date: 22/09/2021
"""

from time import time
from selenium import webdriver

CHROME_DRIVER_PATH = "C:\\Development\\chromedriver"
WEB_URL = "https://orteil.dashnet.org/experiments/cookie/"

STORE = {
    "Cursor - 15": "buyCursor",
    "Grandma - 100": "buyGrandma",
    "Factory - 500": "buyFactory",
    "Mine - 2,000": "buyMine",
    "Shipment - 7,000": "buyShipment",
    "Alchemy lab - 50,000": "buyAlchemy lab",
    "Portal - 1,000,000": "buyPortal",
    "Time machine - 123,456,789": "buyTime machine",
}

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(WEB_URL)

cookie = driver.find_element_by_id("cookie")
start = int(time())
timeout = start + 20

while int(time()) < timeout:
    while int(time()) < start + 5:
        cookie.click()
    grayed_store = driver.find_elements_by_css_selector(".grayed b")
    grayed_store = [item.text for item in grayed_store]
    item_to_buy = driver.find_element_by_id("buyCursor")
    for item in STORE:
        if item not in grayed_store:
            item_to_buy = driver.find_element_by_id(STORE[item])
            item_to_buy.click()
    start = int(time())

total_points = driver.find_element_by_id("money")
print(f"Total Points is {total_points.text}")

driver.quit()
