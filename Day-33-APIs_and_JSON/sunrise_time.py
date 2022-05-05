"""
Program: Sunrise Time
Author: Subhashish Dhar
Date: 04/09/2021
"""

import datetime as dt
import requests

MY_LATITUDE = 12.971599
MY_LONGITUDE = 77.594566

parameters = {"lat": MY_LATITUDE, "lng": MY_LONGITUDE, "formatted": 0}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = dt.datetime.now()

print(f"Sunrise time is {sunrise}")
print(f"Time now is {time_now}")
print(f"Sunset time is {sunset}")
