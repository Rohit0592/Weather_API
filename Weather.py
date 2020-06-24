import json
import requests
import ast
import re

url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
response = requests.get(url)

# To print the status
# print(response)

json_response = json.loads(response.text)
# print (json_response)
try:

    # 1. Is the response contains 4 days of data

    data = []
    for items1 in json_response['list']:
        for new_items1 in items1['dt_txt']:
            # print("Items from the date dict is : " + str(items1['dt_txt']))
            x = re.search("^(\d+-\d+-(\d+))\s+.*$", str(items1['dt_txt']))
            data.append(x.group(2))

    y = set(data)
    Number_of_days = int(max(y)) - int(min(y))

    print("\nResponse contains " + str(Number_of_days) + " days of data")
    print("-----------------------------------------------")

    # 2. Is all the forecast in the hourly interval (no hour should be missed)

    # 3. For all 4 days, the temp should not be less than temp_min and not more than temp_max
    print('For all 4 days, the temp should not be less than temp_min and not more than temp_max\n')
    for items1 in json_response['list']:
        for new_items1 in items1['main']:
            dict_values = ast.literal_eval(json.dumps(items1['main']))
            # print dict_values
            if dict_values['temp_min'] <= dict_values['temp'] >= dict_values['temp_max']:
                print('temp:' + str(dict_values['temp']))
                print('temp_min:' + str(dict_values['temp_min']))
                print('temp_max:' + str(dict_values['temp_max']))
                print("-----------------------------------------------")

    for items in json_response['list']:
        for new_items in items['weather']:

            # 4. If the weather id is 500, the description should be light rain

            if new_items['id'] == 500:
                print ("Id :" + str(new_items['id']) + " and Description :" + str(new_items['description']))
            # print("-----------------------------------------------")

            # 5. If the weather id is 800, the description should be a clear sky

            if new_items['id'] == 800:
                print ("Id :" + str(new_items['id']) + " and Description :" + str(new_items['description']))
            # print("-----------------------------------------------")


except KeyError:
    print("There were problems fetching the data. Please see below for details")
