"""
Program: CHeck internet speed and post that on twitter
Author: Subhashish Dhar
Date: 29/09/2021
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:\\Development\\chromedriver"
TWITTER_URL = "https://twitter.com/i/flow/login"
TWITTER_EMAIL = "subbu.pybot@gmail.com"
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
SPEED_TEST_URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    """The twitter bot class"""

    def __init__(self):
        """initializes the class and creates the web driver"""
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def tweet_at_provider(self, tweet_text):
        """inputs the tweet text and posts it"""
        self.driver.get(TWITTER_URL)
        # Provide username for login
        self.driver.implicitly_wait(5)
        username = self.driver.find_element_by_name("username")
        username.send_keys(TWITTER_EMAIL)
        username.send_keys(Keys.ENTER)
        # Provide password for login
        self.driver.implicitly_wait(2)
        password = self.driver.find_element_by_name("password")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        # Post the tweet
        self.driver.implicitly_wait(3)
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                  '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                  '1]/div/div/div/div/div/div/div/div/div/label/div['
                                                  '1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(tweet_text)
        submit = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div['
                                                   '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                   '1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        submit.click()

    def get_internet_speed(self):
        """conducts the speed test and returns the result as a f string"""
        self.driver.get(SPEED_TEST_URL)
        # Start the speed Test
        self.driver.implicitly_wait(5)
        start_test = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                       '3]/div[1]/a/span[4]')
        start_test.click()
        # Wait for the test to finish
        time.sleep(45)
        # Get the speeds from the result
        download = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                     '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        upload = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                   '3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        provider = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                     '3]/div/div[3]/div/div/div[2]/div[3]/div/div/div[1]/div[3]/div[2]')
        text = f"I am using {provider.text} network.\nDownload Speed: {download.text}\nUpload Speed: {upload.text}"
        return text

    def close_browsers(self):
        """closes all automated browsers"""
        self.driver.quit()


my_bot = InternetSpeedTwitterBot()
tweet_data = my_bot.get_internet_speed()
my_bot.tweet_at_provider(tweet_text=tweet_data)
my_bot.close_browsers()
