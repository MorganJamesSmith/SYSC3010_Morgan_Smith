import http.client
import urllib.parse
import time
key = "classified"
def thermometer(temp_fd):
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        temp_fd.seek(0)
        temp = int(temp_fd.read()) / 1e3 # Get Raspberry Pi CPU temp
        params = urllib.parse.urlencode({'field1': temp, 'key':key })
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(temp)
            print(response.status, response.reason)
            data = response.read()
        except:
            try:
                print("Closing connection")
                conn.close()
            finally:
                break

if __name__ == "__main__":
    temp_fd = open('/sys/class/thermal/thermal_zone0/temp')
    try:
        thermometer(temp_fd)
    finally:
        temp_fd.close()
