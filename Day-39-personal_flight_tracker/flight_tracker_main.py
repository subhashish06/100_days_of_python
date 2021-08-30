# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
from data_manager import DataManager, PRICES_SHEET_URL
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from datetime import datetime, timedelta

START_CITY_CODE = "BLR"

sheet = DataManager()
prices_data = sheet.get_prices_data()

sheet.add_user()
users_data = sheet.get_users_data()

subscribers = [entry['email'] for entry in users_data['users']]
alert = NotificationManager()

# Populate the IATA codes
for entry in prices_data['prices']:
    if entry['iataCode'] == "EMPTY" or entry['iataCode'] == '':
        url = PRICES_SHEET_URL + f"/{entry['id']}"
        city = entry['city']
        search_obj = FlightSearch()
        city_code = search_obj.get_code(city)
        body = {
          "price": {
            "iataCode": city_code,
          }
        }
        sheet.put_value(url, body=body)

# Find cheapest flight and send alert
from_date = datetime.now().strftime("%d/%m/%Y")
to_date = (datetime.now() + timedelta(days=30*6)).strftime("%d/%m/%Y")

for entry in prices_data['prices']:
    url = PRICES_SHEET_URL + f"/{entry['id']}"
    city = entry['iataCode']
    flight_data = FlightData(src=START_CITY_CODE, dst=city,
                             date_from=from_date, date_to=to_date,
                             min_stay=7, max_stay=28, stops=1)
    price = flight_data.get_price()
    departure_city = flight_data.get_source_city()
    departure_airport = flight_data.get_source_airport()
    arrival_city = flight_data.get_destination_city()
    arrival_airport = flight_data.get_destination_airport()
    outbound_date = flight_data.get_start_date()
    inbound_date = flight_data.get_return_date()
    if price != "No Data" and entry['lowestPrice'] != 'No Data' and int(price) < entry['lowestPrice']:
        alert_text = f"Low Price Alert! Only {price} to fly from " \
                     f"{departure_city}-{departure_airport} to {arrival_city}-{arrival_airport}," \
                     f"from {outbound_date} to {inbound_date}."
        alert.send_message(alert_text)
        msg = f"Subject:Flight Club\n\nHi,\n\n{alert_text}\n\nRegards,\nSubhashish"
        for email in subscribers:
            alert.send_email(email, body=msg)
        body = {
            "price": {
                "lowestPrice": price,
            }
        }
        sheet.put_value(url, body=body)
