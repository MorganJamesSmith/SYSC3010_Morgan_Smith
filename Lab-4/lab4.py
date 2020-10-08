#!/usr/bin/env python3

import http.client
import urllib.parse
import time

key = "AT68QYQ94MQEWXL3"

group = "L3-T-2"
email = "MorganSmith@cmail.carleton.ca"
identifier = "d"

headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = http.client.HTTPConnection("api.thingspeak.com:80")

params = urllib.parse.urlencode({'field1': group, 'field2': email, 'field3': identifier, 'key':key })

conn.request("POST", "/update", params, headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
conn.close()
