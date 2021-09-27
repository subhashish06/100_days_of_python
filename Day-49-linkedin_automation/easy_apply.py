"""
Program: Automated Job application in LinkedIn
Author: Subhashish Dhar
Date: 23/09/2021
"""

import os
from selenium import webdriver

CHROME_DRIVER_PATH = "C:\\Development\\chromedriver"
WEB_URL = "https://www.linkedin.com/jobs/search/?currentJobId=2722247480&f_AL=true&f_E=4&geoId=109710172&keywords" \
          "=network%20security&location=Bengaluru%2C%20Karnataka%2C%20India "

LINKEDIN_USERNAME = "subhashish06@gmail.com"
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(WEB_URL)

# Navigate to the required page
signin = driver.find_element_by_css_selector(".nav .nav__button-secondary")
signin.click()
driver.implicitly_wait(2)

# Provide credentials and sign in
username = driver.find_element_by_id("username")
username.send_keys(LINKEDIN_USERNAME)
password = driver.find_element_by_id("password")
password.send_keys(LINKEDIN_PASSWORD)
sign_in = driver.find_element_by_css_selector(".btn__primary--large")
sign_in.click()
driver.implicitly_wait(3)

# Find the top job and click easy apply
top_job = driver.find_element_by_class_name("jobs-search-two-pane__job-card-container--viewport-tracking-2")
top_job.click()
driver.implicitly_wait(2)
save = driver.find_element_by_class_name("jobs-save-button")
save.click()
