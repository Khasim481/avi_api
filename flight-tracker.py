'''
https://opensky-network.org/api/states/all?icao24=4952c6
'''

from flask import json
from flask.json import load
from requests import get
from flask import Flask, request, jsonify

app = Flask(__name__)

url = 'https://opensky-network.org/api/states/all'

@app.route('/')
def root():
    return 'Hello there from flight tracker!!'

@app.route('/track_flight/<transponder>', methods=['GET'])
def track_the_flight(transponder):
    response = get(url + '?icao24={}'.format(transponder))
    if response.ok:
        data = response.json()
    else:
        data = {}
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
