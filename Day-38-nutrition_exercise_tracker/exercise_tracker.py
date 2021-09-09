"""
Program: Exercise Tracker
Author: Subhashish Dhar
Date: 05/09/2021
"""

import os
from datetime import datetime
import requests
import pandas as pd

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

NUTRITION_URL = "https://trackapi.nutritionix.com/v2/natural/nutrients"
EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

SELECTION = False
QUERY = ''
URL_CHOSEN = ''
while not SELECTION:
    URL_CHOSEN = input("Do you want to log exercise or nutrition? E/N : ")
    if URL_CHOSEN.lower() == "e":
        URL = EXERCISE_URL
        QUERY = input("What did you do? ")
        SELECTION = True
    elif URL_CHOSEN.lower() == "n":
        URL = NUTRITION_URL
        QUERY = input("What did you eat or drink? ")
        SELECTION = True
    else:
        print("Choose only one of the options. 'E' or 'N'.")

body = {
    "query": QUERY,

}

if URL_CHOSEN.lower() == "e":
    response = requests.post(URL, headers=header, json=body)
    response_list = response.json()['exercises']
    time_now = datetime.now()
    Date = [time_now.strftime("%d-%m-%Y") for i in range(len(response_list))]
    Time = [time_now.strftime("%H:%M:%S") for i in range(len(response_list))]
    Exercise = [response_list[i]['name'] for i in range(len(response_list))]
    Duration = [response_list[i]['duration_min'] for i in range(len(response_list))]
    Calories = [response_list[i]['nf_calories'] for i in range(len(response_list))]

    new_data_keys = ['Date', 'Time', 'Exercise', 'Duration', 'Calories']
    new_data_value = [Date, Time, Exercise, Duration, Calories]
    new_data_dict = {}
    for _ in range(len(new_data_keys)):
        new_data_dict[new_data_keys[_]] = new_data_value[_]

    new_data = pd.DataFrame(new_data_dict)
    previous_data = pd.read_csv("workouts.csv")
    full_data = previous_data.append(new_data, ignore_index=True)
    print(full_data)
    full_data.to_csv("workouts.csv", index=False)
else:
    response = requests.post(URL, headers=header, json=body)
    response_list = response.json()['foods']
    time_now = datetime.now()
    Date = [time_now.strftime("%d-%m-%Y") for i in range(len(response_list))]
    Time = [time_now.strftime("%H:%M:%S") for i in range(len(response_list))]
    Food = [response_list[i]['food_name'] for i in range(len(response_list))]
    Quantity = [response_list[i]['serving_qty'] for i in range(len(response_list))]
    Calories = [response_list[i]['nf_calories'] for i in range(len(response_list))]

    new_data_keys = ['Date', 'Time', 'Food', 'Quantity', 'Calories']
    new_data_value = [Date, Time, Food, Quantity, Calories]
    new_data_dict = {}
    for _ in range(len(new_data_keys)):
        new_data_dict[new_data_keys[_]] = new_data_value[_]
    new_data = pd.DataFrame(new_data_dict)
    previous_data = pd.read_csv("diet.csv")
    full_data = previous_data.append(new_data, ignore_index=True)
    print(full_data)
    full_data.to_csv("diet.csv", index=False)
