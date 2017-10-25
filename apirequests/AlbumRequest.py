import requests
from GeniusRequest import GeniusRequest

class SongRequest(GeniusRequest):

    def __init__(self, album_id, access_token):
        super(SearchRequest, self).__init__(access_token)
        self.endpoint = "/album/"
        self.album_id = album_id

    def get_url(self):
        return self.base_url + self.endpoint + self.album_id

    def get_params(self):
        return {'access_token': self.access_token}
