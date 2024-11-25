# variables

name = input("What's your name? ")
city = input("Where are you now? ")
temperature = input("What's the temperature? ")

# calculation

calc_fahrenheit = float(temperature) * 9 / 5 + 32
calc_temperature_evening = float(temperature) - 5
f_evening = float(calc_fahrenheit) - 5

# output

greetings = f"Hi {name}, you are currently in {city} with a temperature of {temperature}°C or {calc_fahrenheit}°F. In the evening you will have {calc_temperature_evening}°C or {f_evening}°F. Enjoy your day!"

print(greetings)

# elif challenges
temperature = input("What's the current temperature in your place?")
temperature = int(temperature)
rain = input("Is it raining? (Yes/No)")
rain = rain.lower()

if temperature > 20 and rain == "no":
  print("Enjoy a sunny day!")
elif temperature > 20 and rain == "yes":
  print("Don't forget your umbrella!")
elif temperature < 20 and rain == "no":
  print("Don't forget your jacket!")
else:
  print("Don't forget your umberella and jacket")



# homework w2
city = input("In what city are you? ")
city = city.capitalize()
temperature = input("How many degrees there?")

if temperature and city:
  temperature = int(temperature)
  if temperature < 20:
    print(f"It is currently warm in {city} with a temperature of {temperature}")
  elif temperature >= 10:
    print(f"It is currently chilly in {city} with a temperature of {temperature}")
  else:
    print(f"It is currently cold in {city} with a temperature of {temperature}")
else:
  print("Please try again later and enter a city and temperature")
  
  # challenge w3 lesson 1
  
def city_temperature():
    city = input("What city are you in?")
    temperature = input("What is the current temperature over there?")
    if city_temperature:
      print(f"You are in {city} and it is currently {temperature} degrees")
    else:
      print("You didn't provide a city and temperature")


  city_temperature()
  
# challenge w3 lesson 2
def informatie():
  city = input("What city are you in?")
  temperature = input("What is the current temperature over there?")
  if temperature and city:
      print(f"You are in {city} and it is currently {temperature} degrees")
  else:
    print("You don't provide a city and temperature")

informatie()
informatie()

# functions

def message(city, temperature, humidity=""):
  """Message for weather in certain location"""
  if humidity:
    full_message = (f"The weather in {city} is {temperature} degrees with humidity {humidity}.")
  else:
    full_message = (f"The weather in {city} is {temperature} degrees.")
    
  print(full_message)

message("Rotterdam", "13", "30%")
message("Jakarta", "32")

# homework w3

def dbct():
  """Informatie van weer"""
  city = input("Enter the name of the city: ")
  temperature = input("Enter the temperature of the city: ")
  def ctof():
    temp_f = (int(temperature) * 9 / 5) + 32
    if city and temperature:
      print(f"It is currently {temperature}°C ({temp_f}°F) in {city}.")
    else:
      print("Please enter a city and temperature.")
  ctof()
dbct()

# challenge w4

countries = ["Portugal", "England", "Spain"]
index = 0

for countries in countries:
  print(f"My number {index + 1} country is {countries.title()}.")
  index = index + 1
  
  
# challenge dictionary w4
  # list exercisee
  #create a dictionary of 3 countries
  # print out the dictionary
  # remove your least favorite country
  # print out the dictionary
  # add another country you'd like to visit
  # print out the dictionary
  # display the capital of each country, one at a time, no loop.


wishlist = {
  'Korea': 'Seoul and Nami Island', 
  'Japan': 'Okinawa',
  'Spain': 'Barcelona'
}
print(wishlist)

wishlist['Turkey'] = 'Cappadoccia'
print(wishlist)

print(f"The capital country of Korea is {wishlist['Korea']}")
print(f"The capital country of Japan is {wishlist['Japan']}")
print(f"The capital country of Turkey is {wishlist['Turkey']}")

  # how dictionary works == 'key' : 'values'. jadi ada keyword dan value that is determined in the dictionary. it will helps to grab a specific data in that case.
  
# looping dictionary
  # how to loop the values of the key in dictionary?
  # how we say it is print(values[key])
  
  #looping dictionary exercise
  
wishlist = {
  'Korea': 'Seoul', 
  'Japan': 'Tokyo',
  'England': 'London'
}
index = 0
print("Countries I'd like to visit:")

for countries, capcity in wishlist.items():
  print(f"{index + 1}: {countries} (Capital city: {capcity})")


index = 0
dailytemp = forecast["daily"]

for dailytemp in forecast:
  dailytemp = str(dailytemp)
  print(f"Day {index + 1}: {dailytemp}")
  
# exercise week 4

weather = {
  "city": "Lisbon",
  "country": "Portugal",
  "temperature": "17.94",
  "humidity": "77%"
}

temperature = weather["temperature"]
temperature = round(float(temperature))
tempf = (int(float(temperature)) * 9 / 5) + 32
city = weather["city"]
country = weather["country"]
humid = weather["humidity"]

print(f"It is {temperature} ({tempf}) in {city}, {country}, the humidity level is {humid}")

# data 2
forecast = {
  "city": "Lisbon",
  "country": "Portugal",
  "daily": [
    17.76,
    13.08,
    12.14,
    11.25,
    14.29
  ]
}

print(f"The forecast for {city}, {country} for the next 5 days is:")
index = 0
daily = forecast['daily']
rdaily = round(float(daily[index]))
rdaily = str(rdaily)

for rdaily in forecast["daily"]:
  index = index + 1
  print(f"Day {index}: {round(rdaily)}°C")


w6
import requests
from rich import print

# Get API
def dcw(city):  
  api_key ="d8138dtbade834co3b9b2b32f2260a59"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"
  # Make API request
  response = requests.get(api_url)
  cweather = response.json()
  ctemperature = cweather['temperature']['current']
  ccountry = cweather['country']
  
  print(f"It is currently {round(ctemperature)}°C in {city}, {ccountry}.")


# Input
city = input("Enter city name: ")
city = city.strip()

if city:
  dcw(city)
else:
  print("Please enter a city name.")












