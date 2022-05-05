"""
Program: Email Motivational Quotes
Author: Subhashish Dhar
Date: 04/09/2021
"""

import os
from datetime import datetime
from random import choice
from smtplib import SMTP

date = datetime.now()

with open("quotes.txt", encoding="utf-8") as file_handler:
    quotes = file_handler.readlines()
    quote_of_the_day = choice(quotes)
    print(quote_of_the_day)

PASSWORD = os.environ.get("GMAIL_PASSWORD")

with SMTP("smtp.gmail.com") as mail:
    mail.starttls()
    mail.login(user="subbu.pybot@gmail.com", password=PASSWORD)
    mail.sendmail(
        from_addr="subbu.pybot@gmail.com",
        to_addrs=["subhashish06@gmail.com"],
        msg=f"Subject:Monday Motivation\n\n"
        f"Hi,\n\nQuote of the Day:\n{quote_of_the_day}\n\nStay Motivated!\n\n"
        f"Regards,\nSubhashish",
    )
