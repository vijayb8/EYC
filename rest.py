# -------------------------------------------------------------------------------
# Name:        Python sample historic data client
# Author:      Jan Grimmer
# Created:     20.03.2018
# -------------------------------------------------------------------------------

from http.client import HTTPSConnection
from base64 import b64encode
import json
import pandas
import requests

HOST_STAGING = "sc-hackathon-s.urbanpulse.de"
HOST_PRODUCTION = "sc-hackathon.urbanpulse.de"
PORT_HISTORIC_DATA = 42000

USER_PW = b"hackathon:L33333t+"


def getEventType(host):
    r = requests.get('https://sc-hackathon.urbanpulse.de/UrbanPulseManagement/api/eventtypes',
                     auth=('hackathon', 'L33333t+'))
    # my_json = r.content.decode('utf8').replace("'", '"')
    my_json = json.loads(r.content)
    for eventtype in my_json['eventtypes']:
        if (eventtype['name'] == 'NRWEnvironmentEventType'):
            return eventtype['sensors']
    return None


def getData(host, sid, since, until):
    server = host + ":" + str(PORT_HISTORIC_DATA)

    pathTemplate = "/UrbanPulseData/historic/sensordata?since={0}&until={1}&sid={2}"
    path = pathTemplate.format(since, until, sid)

    connection = HTTPSConnection(server)
    userAndPass = b64encode(USER_PW).decode("ascii")
    headers = {'Authorization': 'Basic %s' % userAndPass}

    connection.request('GET', path, headers=headers)
    response = connection.getresponse()
    data = response.read()
    return data


def main():
    host = HOST_PRODUCTION
    sensors = getEventType(host)
    for sensor in sensors:
        # A list of all sensors can be obtained from https://<HOST>/UrbanPulseManagement/api/sensors with credentials hackathon/L33333t+
        sid = sensor
        since = "2018-04-01T11:18:00.000Z"
        until = "2018-04-22T11:22:00.000Z"

        data = getData(host, sid, since, until)
        wrappedJsonObject = json.loads(data)
        jsonArray = wrappedJsonObject['sensordata']
        for event in jsonArray:
            print("Received: " + json.dumps(event))


if __name__ == '__main__':
    main()
