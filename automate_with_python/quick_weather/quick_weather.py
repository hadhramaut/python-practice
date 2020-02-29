#  Python 3
# Chapter 14. Use OpenWeatherMap API in order to create script which grabs weather info for specified location

import json, requests, sys

if len(sys.argv) < 2:
    print("Usage: quick_weather.py country_code city_name")
    sys.exit()
country_code = sys.argv[1]
location = ' '.join(sys.argv[2:])

api_key = 'fa179a786ad042d947a90f97db2a7322'
loc_list = []

with open('citylist.json', encoding='utf-8') as json_data:
    for line in json_data:
        j = json.loads(line)
        if j["name"] == location and j["country"] == country_code:
            loc_list.append(j["_id"])
    if len(loc_list) > 1:
        print("More than 1 ID are found for current location! Try better!")
        sys.exit()
    elif len(loc_list) == 0:
        print("Not found location with such parameters!")
        sys.exit()
    else:
        print("Found correct ID {0} for current location. Sending API request to server ...".format(loc_list[0]))
json_data.close()

api_req = requests.get('http://api.openweathermap.org/data/2.5/weather?id=' + str(loc_list[0]) + "&APPID=" + api_key)

i = api_req.json()
if api_req.status_code == 200:
    print("Current information is for {0} location in {1} region".format(i["name"], i["sys"]["country"]))
    print("Today there'll be {0} degrees by Celsius with {1} humidity".format(round(i["main"]["temp"] - 273, 2), i["main"]["humidity"]))
    print("Wind speed is {0}".format(i["wind"]["speed"]))
else:
    print("Error occurred during request processing... Finishing the program")
    sys.exit()