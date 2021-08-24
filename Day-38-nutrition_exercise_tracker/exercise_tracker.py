import os
import requests
import pandas as pd
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

nutrition_url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

url_selected = False
query_string = ''
chosen_url = ''
while not url_selected:
    chosen_url = input("Do you want to log exercise or nutrition? E/N : ")
    if chosen_url.lower() == "e":
        url = exercise_url
        query_string = input("What did you do? ")
        url_selected = True
    elif chosen_url.lower() == "n":
        url = nutrition_url
        query_string = input("What did you eat or drink? ")
        url_selected = True
    else:
        print("Choose only one of the options. 'E' or 'N'.")

body = {
    "query": query_string,
}

if chosen_url.lower() == "e":
    response = requests.post(url, headers=header, json=body)
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
    response = requests.post(url, headers=header, json=body)
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
