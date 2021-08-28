import requests
import os

URL = "https://tequila-api.kiwi.com/v2/search"
APIKEY = os.environ.get("FLIGHT_APIKEY")


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, src, dst, date_from, date_to, min_stay, max_stay, currency="INR", stops=0):
        header = {"apikey": APIKEY}
        parameters = {
            "fly_from": src,
            "fly_to": dst,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": min_stay,
            "nights_in_dst_to": max_stay,
            "one_for_city": 1,
            "curr": currency,
            "max_stopovers": stops
        }
        self.response = requests.get(url=URL, headers=header, params=parameters)

    def get_response(self):
        return self.response.json()

    def get_price(self):
        try:
            return self.response.json()['data'][0]['price']
        except IndexError:
            return 'No Data'

    def get_destination_city(self):
        try:
            return self.response.json()['data'][0]['cityTo']
        except IndexError:
            return 'No Data'

    def get_destination_airport(self):
        try:
            return self.response.json()['data'][0]['flyTo']
        except IndexError:
            return 'No Data'

    def get_source_city(self):
        try:
            return self.response.json()['data'][0]['cityFrom']
        except IndexError:
            return 'No Data'

    def get_source_airport(self):
        try:
            return self.response.json()['data'][0]['flyFrom']
        except IndexError:
            return 'No Data'

    def get_start_date(self):
        try:
            return self.response.json()['data'][0]['route'][0]['local_departure']
        except IndexError:
            return 'No Data'

    def get_return_date(self):
        try:
            return self.response.json()['data'][0]['route'][1]['local_arrival']
        except IndexError:
            return 'No Data'
