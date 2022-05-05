"""
Program: Class that fetches the information from property search site
Author: Subhashish Dhar
Date: 02/10/2021
"""

import requests
from bs4 import BeautifulSoup


class PropertySearch:
    """Class that fetches the information from property search site"""

    def __init__(self, url, headers):
        """
        requests the webpage information in the url and creates the BeautifulSoup object.
        """
        self.headers = headers
        self.url = url
        response = requests.get(url, headers=headers)
        self.soup = BeautifulSoup(response.text, features="lxml")

    def get_prices(self):
        """gets the prices in the listings"""
        price_list = [
            price.get_text()
            for price in self.soup.find_all("div", class_="list-card-price")
        ]
        return price_list

    def get_addresses(self):
        """gets the addresses in the listings"""
        address_list = [
            address.get_text()
            for address in self.soup.find_all("address", class_="list-card-addr")
        ]
        return address_list

    def get_links(self):
        """gets the links in the listings"""
        link_list = [
            link.get("href") for link in self.soup.find_all("a", class_="list-card-img")
        ]
        return link_list
