import requests
import os

URL = "https://tequila-api.kiwi.com/locations/query"
APIKEY = os.environ.get("FLIGHT_APIKEY")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    @staticmethod
    def get_code(city):
        header = {"apikey": APIKEY}
        parameters = {"term": city}
        response = requests.get(url=URL, headers=header, params=parameters)
        return response.json()["locations"][0]["code"]
