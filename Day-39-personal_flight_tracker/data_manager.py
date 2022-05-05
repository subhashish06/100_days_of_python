"""
Program: Flight Club Data Manager
Author: Subhashish Dhar
Date: 05/09/2021
"""

import os
import requests

PRICES_SHEET_URL = os.environ.get("SHEET_URL")
USERS_SHEET_URL = (
    "https://api.sheety.co/41c17aa0e46236e4225bd96218dacaae/flightDeals/users"
)


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    @staticmethod
    def get_prices_data():
        """gets the price from sheet"""
        response = requests.get(PRICES_SHEET_URL)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_users_data():
        """gets the users from sheet"""
        response = requests.get(USERS_SHEET_URL)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def put_value(url, body):
        """puts the edited value in the sheet"""
        response = requests.put(url, json=body)
        response.raise_for_status()
        return response.text

    @staticmethod
    def add_user():
        """adds an user to the sheet"""
        more_email = True
        while more_email:
            user_choice = input("Do you want to add an user? (yes/no) : ")
            if user_choice.lower() == "no":
                more_email = False
            else:
                first_name = input("Enter your first name : ")
                last_name = input("Enter your last name : ")
                email = input("Enter your email address : ")
                body = {
                    "user": {
                        "firstName": first_name,
                        "lastName": last_name,
                        "email": email,
                    }
                }
                response = requests.post(url=USERS_SHEET_URL, json=body)
                response.raise_for_status()
