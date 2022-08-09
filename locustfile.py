from locust import HttpUser, task
from json import load


class QuickstartUser(HttpUser):
    country_list = []
    @task(1)
    def avi_api(self):
        all_flights = self.client.get("/get_all_flight_states").json()

        for flight in all_flights:
            self.client.get(
                "/track_flight/{}".format(flight["icao24"]), name="/track_flight/*")

        for country in self.country_list:
            self.client.get("/country_air_space" + country, name="/country_air_space/*")

    @task(100)
    def avi_api_general(self):
        self.client.get("/get_all_flight_states")
        self.client.get("/country_air_space?lamin=45.8389&lomin=5.9962&lamax=47.8229&lomax=10.5226")
        self.client.get("/track_flight/4b1814")

    def on_start(self):
        self.country_list.clear()
        with open("geo_data.json", "r") as file:
            json_data = load(file)
            for country in json_data.values():
                lamin = country['sw']['lat']
                lamax = country['ne']['lat']
                lomin = country['sw']['lon']
                lomax = country['ne']['lon']
                self.country_list.append('?lamin={0}&lomin={1}&lamax={2}&lomax={3}'.format(
                    lamin, lomin, lamax, lomax))
        return super().on_start()
