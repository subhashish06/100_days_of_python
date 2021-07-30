from twilio.rest import Client
import requests

API_KEY = "64671c189476dcfdbb3309e18f10c7b8"
LATITUDE = 24.819799
LONGITUDE = 79.145599

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
    "units": "metric"
}

account_sid = 'AC563da7de98225d587e5aea9ab11b275d'
auth_token = 'fd07b208690287722533d3d1c2852ef7'

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for i in range(12):
    rain_code = weather_data["hourly"][i]["weather"][0]["id"]
    print(rain_code)
    if int(rain_code) < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='It might rain. Bring an Umbrella!',
            to='whatsapp:+919739983563'
            )

    print(message.status)
