import requests
import os
from pprint import pprint

SHEET_URL = os.environ.get("SHEET_URL")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(SHEET_URL)
        self.response.raise_for_status()
        self.data = self.response.json()['prices']

    def get_data(self):
        return self.response.json()

    def write_entry(self, url, body):
        self.response = requests.put(url, json=body)
        self.response.raise_for_status()
        return self.response.text
