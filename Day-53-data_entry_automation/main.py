"""
Program: Scrape website for property prices and create a google sheet for the data.
Author: Subhashish Dhar
Date: 02/10/2021
"""

from property_search import PropertySearch
from form_filler import FormFiller

CHROME_DRIVER_PATH = "C:\\Development\\chromedriver"
GOOGLE_FORM_LINK = (
    "https://docs.google.com/forms/d/e/1FAIpQLSfvA6w4rQQM9Fe_9TifE6qclxrQyy8TIRUHZDKzOwoGF-0dSQ"
    "/viewform?usp=sf_link "
)
ZILLOW_URL = (
    "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C"
    "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A"
    "-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C"
    "%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A"
    "%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse"
    "%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B"
    "%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D"
    "%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min"
    "%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D "
)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/94.0.4606.61 Safari/537.36 ",
    "Accept-Language": "en-US",
}

properties = PropertySearch(ZILLOW_URL, headers=headers)
addresses = properties.get_addresses()
prices = properties.get_prices()
links = properties.get_links()

form_filler = FormFiller(GOOGLE_FORM_LINK, driver_path=CHROME_DRIVER_PATH)
form_filler.fill_form(addresses, prices, links)
form_filler.close_browser()
