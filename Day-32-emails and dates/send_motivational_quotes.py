from smtplib import SMTP
from datetime import datetime
from random import choice

date = datetime.now()

if date.weekday() == 0:
    with open("quotes.txt") as f:
        quotes = f.readlines()
        quote_of_the_day = choice(quotes)
        print(quote_of_the_day)

    with SMTP("smtp.gmail.com") as mail:
        mail.starttls()
        mail.login(user="subhashish.py@gmail.com", password="Python@123")
        mail.sendmail(
                    from_addr="subhashish.py@gmail.com",
                    to_addrs=["subhashish06@gmail.com", "bananivista2017@gmail.com"],
                    msg=f"Subject:Monday Motivation\n\n"
                        f"Hi,\n\nQuote of the Day:\n{quote_of_the_day}\n\nStay Motivated!\n\n"
                        f"Regards,\nSubhashish"
                    )
