from twilio.rest import Client
import requests
import os

API_KEY = os.environ.get("OWM_API_KEY")
LATITUDE = 12.971599
LONGITUDE = 77.594566

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "exclude": "hourly,minutely,daily",
    "units": "metric"
}

account_sid = 'AC563da7de98225d587e5aea9ab11b275d'
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

temperature = weather_data["current"]["temp"]
weather = weather_data["current"]["weather"][0]["description"]

client = Client(account_sid, auth_token)
# WhatsAPP
message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'Currently in Bangalore:\n\nTemperature : {temperature}\nWeather : {weather}',
        to='whatsapp:+919739983563'
        )

print(message.sid)
# SMS
message = client.messages.create(
    messaging_service_sid='MG3db36b400f9d11a13e0c50d9c110e45f',
    body=f'Currently in Bangalore:\n\nTemperature : {temperature}\nWeather : {weather}',
    to='+919739983563'
    )

print(message.sid)
