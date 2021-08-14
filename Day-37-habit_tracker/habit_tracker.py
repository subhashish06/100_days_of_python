from datetime import datetime
import requests
import os

TOKEN = os.environ.get("PIXELA_TOKEN")
BASE_URL = "https://pixe.la"
USERNAME = "subbu06"


# Create a user
def create_user():
    url = BASE_URL + "/v1/users"
    parameters = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url, json=parameters)
    print(response.text)


# Create a new graph
def create_graph(graph_id, graph_name, unit="numbers", datatype="int", color="ajisai"):
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


# Get the graph
def get_graph(graph_id):
    url = BASE_URL + f"/v1/users/{USERNAME}/graphs/{graph_id}"

    response = requests.get(url)
    print(response.text)


# Post a pixel
def post_pixel(graph_id, date, number):
    url = BASE_URL + f"/v1/users/{USERNAME}/graphs/{graph_id}"
    header = {"X-USER-TOKEN": TOKEN}
    pixel_data = {
        "date": date,
        "quantity": number,
    }

    response = requests.post(url, headers=header, json=pixel_data)
    print(response.text)


# Update a pixel
def update_pixel(graph_id, date, number):
    url = BASE_URL + f"/v1/users/{USERNAME}/graphs/{graph_id}/{date}"
    header = {"X-USER-TOKEN": TOKEN}
    updated_data = {"quantity": number}

    response = requests.put(url, headers=header, json=updated_data)
    print(response.text)


# Delete a pixel
def delete_pixel(graph_id, date):
    url = BASE_URL + f"/v1/users/{USERNAME}/graphs/{graph_id}/{date}"
    header = {"X-USER-TOKEN": TOKEN}

    response = requests.delete(url, headers=header)
    print(response.text)


# create_user()
# create_graph("graph1", "smoking_habit", unit="cigarettes")
# get_graph("graph1")

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

post_pixel("graph1", formatted_date, "4")
# update_pixel("graph1", formatted_date, "5")
# delete_pixel("graph1", formatted_date)
