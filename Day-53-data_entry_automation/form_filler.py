"""
Program: Class that fills the google form
Author: Subhashish Dhar
Date: 02/10/2021
"""

from selenium import webdriver


class FormFiller:
    """Class that fills the google form"""
    def __init__(self, url, driver_path):
        """initialises the webdriver and opens the url webpage"""
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get(url)

    def fill_form(self, address, price, link):
        """fills the form with the information provided"""
        if len(address) != len(price) and len(address) != len(link):
            raise "The lists should have equal number of entries!"
        for index in range(len(address)):
            address_input = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                '1]/div/div[1]/input')
            address_input.click()
            address_input.send_keys(address[index])

            price_input = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                '1]/div/div[1]/input')
            price_input.click()
            price_input.send_keys(price[index].split("+")[0])

            link_input = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                '1]/div/div[1]/input')
            link_input.click()
            link_input.send_keys(link[index])
            submit = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit.click()

            self.driver.implicitly_wait(2)
            submit_another = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            submit_another.click()
            self.driver.implicitly_wait(2)

    def close_browser(self):
        """closes the browser"""
        self.driver.quit()
