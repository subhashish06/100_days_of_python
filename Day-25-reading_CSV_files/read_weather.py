# with open('weather_data.csv', mode='r') as f:
#     data = f.readlines()

# import csv
#
# with open('weather_data.csv', mode='r') as f:
#     data = csv.reader(f)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)


import pandas as pd

data = pd.read_csv('weather_data.csv')
# print(data)
# print(data['temp'])
# data_list = data['temp'].to_list()
# print(f"The avg temperature is : {data['temp'].mean()}")
# print(f"Total number of entries are {len(data_list)}")
# print(data.describe())
# print(data.dtypes)
# data.to_excel('weather.xls', sheet_name='Weather', index=False)
# print(data.info())
# data_dict = data.to_dict()
# print(data_dict)
# print(data[data.condition == 'Sunny'].day)
sunny_days = data[data.condition == 'Sunny'].day.to_list()
print(sunny_days)