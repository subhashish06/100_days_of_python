"""
Program: Stock Update
Author: Subhashish Dhar
Date: 04/09/2021
"""

import os
import requests
from twilio.rest import Client

STOCK = "INFN"
COMPANY_NAME = "Infinera"

# Get the Stock Price Movement
stock_api_key = os.environ.get("STOCK_AUTH_TOKEN")
STOCK_URL = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "GLOBAL_QUOTE",
    "symbol": STOCK,
    "apikey": stock_api_key,
}

stock_response = requests.get(url=STOCK_URL, params=stock_parameters)
stock_response.raise_for_status()
stock_price_details = stock_response.json()
stock_movement = stock_price_details["Global Quote"]["10. change percent"][:4]
print(stock_movement)
stock_price = stock_price_details["Global Quote"]["05. price"][:-2]
print(stock_price)

# Get the News
news_api_key = os.environ.get("NEWS_AUTH_TOKEN")
NEWS_URL = "https://newsapi.org/v2/everything"
parameters = {"apiKey": news_api_key, "qInTitle": COMPANY_NAME, "sortBy": "relevancy"}

news_response = requests.get(NEWS_URL, params=parameters)
news_response.raise_for_status()
news_collection = news_response.json()
news_title = news_collection["articles"][0]["title"]
print(news_title)
news_description = news_collection["articles"][0]["description"]
print(news_description)

# Send SMS
SID = "AC563da7de98225d587e5aea9ab11b275d"
twilio_api_key = os.environ.get("TWILIO_AUTH_TOKEN")

if float(stock_movement) > 0:
    message_text = (
        f"{STOCK}: {stock_price} 🔺{stock_movement}%\n\n"
        f"Headline : {news_title}\n\nBrief : {news_description}"
    )
else:
    message_text = (
        f"{STOCK}: {stock_price} 🔻{stock_movement}%\n\n"
        f"Headline : {news_title}\n\nBrief : {news_description}"
    )

client = Client(SID, twilio_api_key)
message = client.messages.create(
    messaging_service_sid="MG3db36b400f9d11a13e0c50d9c110e45f",
    body=message_text,
    to="+919739983563",
)

print(message.sid)
