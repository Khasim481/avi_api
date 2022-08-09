'''
https://opensky-network.org/api/states/all?lamin=45.8389&lomin=5.9962&lamax=47.8229&lomax=10.5226
'''

from flask.json import load
from requests import get
from flask import Flask, request, jsonify

app = Flask(__name__)

# url = 'https://opensky-network.org/api/states/all?lamin={0}&lomin={1}&lamax={2}&lomax={3}'.format('45.8389', '5.9962','47.8229','10.5226')

url = 'https://opensky-network.org/api/states/all'
state_foramt = ["icao24", "callsign", "origin_country", "time_position", "last_contact",
                "longitude", "latitude", "baro_altitude", "on_ground", "velocity", "true_track",
                "vertical_rate", "sensors", "geo_altitude", "squawk", "spi", "position_source"]

@app.route('/')
def root():
    return 'Hello there from container!!'

@app.route('/get_all_flight_states', methods=['GET'])
def get_all_flight_states():
    response = get(url)
    if response.ok:
        # data = response.json()
        data = [dict(zip(state_foramt, state)) for state in response.json()['states']]
    else:
        data = {}
    return jsonify(data)

def parse_grounded_and_flying_state(flights):
    data = {"grounded": [], "flying": []}
    { data['grounded'].append(flight) if flight['on_ground'] else data['flying'].append(flight) for flight in flights }
    return jsonify(data)

def watch_country_air_space(data):
    countries = load(open('avi_api\world_data.json'))
    for flight in data['flying']:
        country = countries[flight['origin_country']]

@app.route('/get_data_of_flight_in_air', methods=['POST'])
def get_data_of_flight_in_air(lamin, lomin, lamax, lomax):
    lamax, lamin, lomax, lomin = request.args.get('lamax', ''), request.args.get('lamin', ''), request.args.get('lomax'), request.args.get('lomin')
    data = get(url + '?lamin={0}&lomin={1}&lamax={2}&lomax={3}'.format(lamin, lomin, lamax, lomax)).json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
