import http.client, urllib
import json

https = "shopper-api.instacart.com"
hR = "/driver/virtual_batches"

### Sample Json Code
# {
#     "accuracy": 3.9,
#     "direction": 0.0,
#     "is_considered_mock": false,
#     "is_mock": false,
#     "latitude": [LATITUDE_ON_CONFIG],
#     "longitude": [LONGITUDE_ON_CONFIG],
#     "measured_at": "2019-10-20T21:27:36.000+0000 [of course here you set the timestampo with python]",
#     "speed": 0.0,
#     "track_location_response": true
# }
### Can customize below conditions
# ## Please run Xampp first to test
#https = "10.100.2.34"
#hR = "/api.php"

hrToAccept = "/driver/virtual_batches/delivery"
key1 = 'latitude'
key2 = 'longitude'

### Checking json object exist
class Response:

    def __init__(self, data):
        self.__dict__ = json.loads(data)

### Accept
def Accept():
    connA = http.client.HTTPConnection(https, 80)
    connA.connect()
    connA.request("GET", hrToAccept)
    connA.close()

bLoop = True

print("Start connection")

conn = http.client.HTTPSConnection(https)
conn.connect()

print("Next")

i = 1
while bLoop:
    print(i)
    i += 1
    conn.request("GET", hR)
    response = conn.getresponse()
    data = response.read()
    res = Response(data)

    print(data)

conn.close()
