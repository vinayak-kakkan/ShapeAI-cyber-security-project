import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

f = open('log2.txt', 'w')
f.write("-------------------------------------------------------------")
f.write("\n")
f.write("Weather Stats for - ")
f.write(location.upper())
f.write(" || ")
f.write(date_time)
f.write("\n")
f.write("-------------------------------------------------------------")
f.write("\n")
f.write("current temperature is:")
strtemp=str(temp_city)
f.write(strtemp[0:5])
f.write(" deg C")
f.write("\n")
f.write("current wheather desc : ")
f.write(weather_desc)
f.write("\n")
f.write("current humidity      : ")
strhmdt=str(hmdt)
f.write(strhmdt[0:3])
f.write(" %")
f.write("\n")
f.write("current wind speed    : ")
f.write(str(wind_spd))
f.write(" kmph")
f.write("\n")
f.close()