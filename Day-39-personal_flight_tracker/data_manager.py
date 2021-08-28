import requests
import os
from pprint import pprint

PRICES_SHEET_URL = os.environ.get("SHEET_URL")
USERS_SHEET_URL = "https://api.sheety.co/41c17aa0e46236e4225bd96218dacaae/flightDeals/users"

class DataManager:
    # This class is responsible for talking to the Google Sheet.

    @staticmethod
    def get_prices_data():
        response = requests.get(PRICES_SHEET_URL)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_users_data():
        response = requests.get(USERS_SHEET_URL)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def put_value(url, body):
        response = requests.put(url, json=body)
        response.raise_for_status()
        return response.text

    @staticmethod
    def add_user():
        more_email = True
        while more_email:
            user_choice = input("Do you want to add an user? (yes/no) : ")
            if user_choice.lower() == 'no':
                more_email = False
            else:
                fn = input("Enter your first name : ")
                ln = input("Enter your last name : ")
                email = input("Enter your email address : ")
                body = {
                            "user": {
                                "firstName": fn,
                                "lastName": ln,
                                "email":email
                            }
                        }
                response = requests.post(url=USERS_SHEET_URL, json=body)
                response.raise_for_status()
