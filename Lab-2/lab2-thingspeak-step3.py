import urllib.request
import requests
import json

from random import randint

READ_API_KEY="classified"
WRITE_API_KEY="classified"
CHANNEL_NUMBER="classified"

def thingspeak_post(field1, field2):
    "Posts data to the server"
    BASE_URL='https://api.thingspeak.com/update?api_key='
    HEADER='&field1={}&field2={}'.format(field1, field2)
    URL=BASE_URL+WRITE_API_KEY+HEADER
    print("Posting data to: " + URL)
    print("field1=" + str(field1) + ", field2=" + str(field2))
    print()

    data=urllib.request.urlopen(URL)

def read_data_thingspeak():
    "Fetches data from the server"
    BASE_URL='https://api.thingspeak.com/channels/' + CHANNEL_NUMBER + '/feeds.json?api_key='
    HEADER='&results=1'
    URL=BASE_URL+READ_API_KEY+HEADER
    print("Fetching data from: " + URL)

    data=requests.get(URL).json()

    channel_id=data['channel']['id']

    field1=data['feeds'][0]['field1']
    field2=data['feeds'][0]['field2']

    print("Fetching complete. field1=" + str(field1) + ", field2=" + str(field2))
    print()


if __name__ == '__main__':
    thingspeak_post(randint(1,30), randint(1,30))
    read_data_thingspeak()
