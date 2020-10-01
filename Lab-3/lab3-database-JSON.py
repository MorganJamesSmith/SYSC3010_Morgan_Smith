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
                            tdate DATE NOT NULL,
                            ttime TIME NOT NULL,
                            city TEXT NOT NULL,
                            temp REAL NOT NULL,
                            humidity INTEGER NOT NULL,
                            pressure INTEGER NOT NULL,
                            windspeed REAL NOT NULL
                                        ); """
    try:
        c = conn.cursor()
        c.execute(weather_table)
    except Error as e:
        print(e)

def database_insert_weather(values):
    try:
        c = conn.cursor()
        c.execute('''INSERT INTO weather VALUES(date('now'), time('now'), ?, ?, ?, ?, ?)''', values)
    except Error as e:
        print(e)

def database_fetch_weather():
        c = conn.cursor()
        c.execute('''SELECT * FROM weather''')
        return c


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
conn.commit()

db_data = database_fetch_weather();
for row in db_data:
    print(row)

# So I've gotten the data into the database, but now I need to figure
# out how to select only the latest date, and how to actually get the
# data out of the cursor

database_disconnect()


degreeSym = chr(176)

print ("Temperature: %d%sF" % (data["main"]["temp"], degreeSym ))
print ("Humidity: %d%%" % data["main"]["humidity"])
print ("Pressure: %d" % data["main"]["pressure"] )
print ("Wind : %d" % data["wind"]["speed"])
