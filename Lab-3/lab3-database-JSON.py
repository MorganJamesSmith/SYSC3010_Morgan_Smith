from urllib.request import *
from urllib.parse import *
import json
import sqlite3
from sqlite3 import Error

conn = None

def database_connect(db_file):
    global conn
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

def database_disconnect():
    if conn:
        conn.close()

def database_create_table():
    weather_table = """ CREATE TABLE IF NOT EXISTS weather (
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
                            city TEXT NOT NULL,
                            temp REAL NOT NULL,
                            humidity INTEGER NOT NULL,
                            pressure INTEGER NOT NULL,
                            windspeed REAL NOT NULL
                                        ); """
    with conn:
        conn.execute(weather_table)

def database_insert_weather(values):
    with conn:
        conn.execute('''INSERT INTO weather (city, temp, humidity, pressure, windspeed) VALUES(?, ?, ?, ?, ?)''', values)

def database_fetch_weather():
        return conn.execute('''SELECT temp, humidity, pressure, windspeed FROM weather ORDER BY timestamp DESC LIMIT 1''')


def obtain_weather_data(city):
    # The URL that is formatted:
    # http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa

    # As of October 2015, you need an API key.
    # I have registered under my Carleton email.
    apiKey = "a808bbf30202728efca23e099a4eecc7"

    # Build the URL parameters
    params = {"q":city, "units":"imperial", "APPID":apiKey }
    arguments = urlencode(params)

    # Get the weather information
    address = "http://api.openweathermap.org/data/2.5/weather"
    url = address + "?" + arguments

    webData = urlopen(url)
    results = webData.read().decode('utf-8')
    # results is a JSON string
    webData.close()

    #Convert the json result to a dictionary
    # See http://openweathermap.org/current#current_JSON for the API

    data = json.loads(results)
    return data


# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

data = obtain_weather_data(city)

database_connect("weather.db")
database_create_table()
values = (data["name"], data["main"]["temp"], data["main"]["humidity"], data["main"]["pressure"], data["wind"]["speed"])
database_insert_weather(values)

degreeSym = chr(176)
db_data = database_fetch_weather();
for row in db_data:
    print ("Temperature: %d%sF" % (row[0], degreeSym))
    print ("Humidity: %d%%" % row[1])
    print ("Pressure: %d" % row[2])
    print ("Wind : %d" % row[3])


database_disconnect()
