'''
https://opensky-network.org/api/states/all?lamin=45.8389&lomin=5.9962&lamax=47.8229&lomax=10.5226
'''

from flask.json import load
from requests import get
from flask import Flask, request, jsonify

app = Flask(__name__)

# url = 'https://opensky-network.org/api/states/all?lamin={0}&lomin={1}&lamax={2}&lomax={3}'.format('45.8389', '5.9962','47.8229','10.5226')

url = 'https://opensky-network.org/api/states/all'


@app.route('/')
def root():
    return 'Hello there from country air space!!'

@app.route('/country_air_space', methods=['GET'])
def get_data_of_flight_in_air():
    lamax, lamin, lomax, lomin = request.args.get('lamax', ''), request.args.get(
        'lamin', ''), request.args.get('lomax', ''), request.args.get('lomin', '')
    response = get(url + '?lamin={0}&lomin={1}&lamax={2}&lomax={3}'.format(lamin, lomin, lamax, lomax))
    if response.ok:
        data = response.json()
    else:
        data = {}
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
