"""
Program: Amazon Price Tracker
Author: Subhashish Dhar
Date: 14/09/2021
"""

import os
from smtplib import SMTP
import requests
from bs4 import BeautifulSoup

# Getting the price from Amazon
URL = "https://www.amazon.in/dp/B08HHMMRMR/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B08HHMMRMR&pd_rd_w=avmM8&pf_rd_p=4e9225d2-7473-4eb0-95d5-670190275218&pd_rd_wg=soOHD&pf_rd_r=80CMCY0D5XHMVJM8W1B5&pd_rd_r=608645b6-1a94-4db1-95f2-79638b97bbd5&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUjVaVTdUWFBGWEtYJmVuY3J5cHRlZElkPUEwMDk2MzQ0MVFRR05aOE1CNVc3RyZlbmNyeXB0ZWRBZElkPUEwMTgwMDI5Mk1ZMlFZVlk2NUU3NCZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.text, features="lxml")

price = soup.find(id="priceblock_ourprice").text
price = price.replace(',', '')
price = price[1:]
price = price.split(".")[0]
price = int(price)

# Send the email.
PASSWORD = os.environ.get("GMAIL_PASSWORD")

with SMTP("smtp.gmail.com") as mail:
    mail.starttls()
    mail.login(user="subbu.pybot@gmail.com", password=PASSWORD)
    mail.sendmail(
        from_addr="subbu.pybot@gmail.com",
        to_addrs="subhashish06@gmail.com",
        msg=f"Subject:Price Drop Alert\n\n"
            f"The Panasonic Fridge is now available for {price}\n\n"
            f"Regards,\nSubhashish Python Bot"
    )
