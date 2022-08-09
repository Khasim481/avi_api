'''
https://opensky-network.org/api/states/all?lamin=45.8389&lomin=5.9962&lamax=47.8229&lomax=10.5226
'''

from flask import json
from flask.json import load
from requests import get
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# url = 'https://opensky-network.org/api/states/all?lamin={0}&lomin={1}&lamax={2}&lomax={3}'.format('45.8389', '5.9962','47.8229','10.5226')

url = 'https://opensky-network.org/api/states/all'
state_foramt = ["icao24", "callsign", "origin_country", "time_position", "last_contact",
                "longitude", "latitude", "baro_altitude", "on_ground", "velocity", "true_track",
                "vertical_rate", "sensors", "geo_altitude", "squawk", "spi", "position_source"]


all_flights = get("http://avi-api.com/get_all_flight_states").json()["states"]
for flight in all_flights:
    get("http://avi-api.com/track_flight/{}".format(flight["icao24"]))
with open("geo_data.json", "w") as file:
    json_data = load(file)
    for country in json_data:
        lamin = country['sw']['lat']
        lamax = country['ne']['lat']
        lomin = country['sw']['lon']
        lomax = country['ne']['lon']
        get(url + '?lamin={0}&lomin={1}&lamax={2}&lomax={3}'.format(lamin, lomin, lamax, lomax))
