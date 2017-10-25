import requests

class SongRequest(GeniusRequest):

    def __init__(self, song_id, access_token):
        super(SearchRequest, self).__init__(access_token)
        self.endpoint = "/song/"
        self.song_id = song_id

    def get_url(self):
        return self.base_url + self.endpoint + self.song_id

    def get_params(self):
        return {'access_token': self.access_token}
