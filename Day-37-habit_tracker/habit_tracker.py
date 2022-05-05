"""
Program: Habit Tracker
Author: Subhashish Dhar
Date: 05/09/2021
"""

import os
from datetime import datetime
import requests

TOKEN = os.environ.get("PIXELA_TOKEN")
BASE_URL = "https://pixe.la"
USERNAME = "subbu06"


def create_user():
    """create a user"""
    url = BASE_URL + "/v1/users"
    parameters = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url, json=parameters)
    print(response.text)


def create_graph(graph_id, graph_name, unit="numbers", datatype="int", color="ajisai"):
    """Create a new graph"""
    url = BASE_URL + f"/v1/users/{USERNAME}/graphs"
    header = {"X-USER-TOKEN": TOKEN}
    parameters = {
        "id": graph_id,
        "name": graph_name,
        "unit": unit,
        "type": datatype,
        "color": color,
    }

    response = requests.post(url, headers=header, json=parameters)
    print(response.text)


def get_graph(graph_id):
    """Get the graph"""
    url = BASE_URL + f"/v1/users/{USERNAME}/graphs/{graph_id}"

    response = requests.get(url)
    print(response.text)


def post_pixel(graph_id, date):
    """posts a pixel"""
    url = BASE_URL + f"/v1/users/{USERNAME}/graphs/{graph_id}"
    header = {"X-USER-TOKEN": TOKEN}
    pixel_data = {
        "date": date,
        "quantity": input("How many cigarettes smoked today?"),
    }

    response = requests.post(url, headers=header, json=pixel_data)
    print(response.text)


def update_pixel(graph_id, date, number):
    """updates a pixel"""
    url = BASE_URL + f"/v1/users/{USERNAME}/graphs/{graph_id}/{date}"
    header = {"X-USER-TOKEN": TOKEN}
    updated_data = {"quantity": number}

    response = requests.put(url, headers=header, json=updated_data)
    print(response.text)


def delete_pixel(graph_id, date):
    """deletes a pixel"""
    url = BASE_URL + f"/v1/users/{USERNAME}/graphs/{graph_id}/{date}"
    header = {"X-USER-TOKEN": TOKEN}

    response = requests.delete(url, headers=header)
    print(response.text)


# create_user()
# create_graph("graph1", "smoking_habit", unit="cigarettes")
# get_graph("graph1")

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

post_pixel("graph1", formatted_date)
# update_pixel("graph1", formatted_date, "5")
# delete_pixel("graph1", formatted_date)
