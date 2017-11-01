import requests
from GeniusRequest import GeniusRequest
from model.Track import Track

class SongRequest(GeniusRequest):

    def __init__(self, song_id, access_token):
        super(SongRequest, self).__init__(access_token)
        self.endpoint = "/songs/"
        self.song_id = song_id

    def get_url(self):
        return self.base_url + self.endpoint + str(self.song_id)

    def get_params(self):
        return {'access_token': self.access_token}

    def execute(self):
        try:
            response = requests.get(self.get_url(), self.get_params())
            track = self.transform_response(response)
            return track
        except Exception as e:
            print "Error retrieving data from " + self.get_url()
            print e

    def transform_response(self, response):
        response_json = response.json()
        song_json = response_json["response"]["song"]

        title = song_json["title_with_featured"]
        primary_artist = song_json["primary_artist"]["name"]

        producers = ""
        for producer in song_json["producer_artists"]:
            producers += producer["name"] + ", "
        producers = producers[0:-2]

        return Track(self.song_id, title, primary_artist, producers)
