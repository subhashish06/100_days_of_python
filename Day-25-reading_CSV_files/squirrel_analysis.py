"""
Program: Squirrel Analyzer
Author: Subhashish Dhar
Date: 03/09/2021
"""

import pandas as pd

data = pd.read_csv("Squirrel_Data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

new_data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Numbers": [gray_squirrels, black_squirrels, cinnamon_squirrels],
}

squirrel_numbers_df = pd.DataFrame(data=new_data_dict)
squirrel_numbers_df.to_csv("squirrel_numbers.csv", index=False)
