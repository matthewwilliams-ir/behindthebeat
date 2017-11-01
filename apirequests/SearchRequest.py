import requests
from GeniusRequest import GeniusRequest

class SearchRequest(GeniusRequest):

    def __init__(self, query, access_token):
        super(SearchRequest, self).__init__(access_token)
        self.endpoint = "/search"
        self.query = query

    def get_url(self):
        return self.base_url + self.endpoint

    def get_params(self):
        return {'q': self.query, 'access_token': self.access_token}

    def execute(self):
        try:
            response = requests.get(self.get_url(), self.get_params())
            song_id = self.transform_response(response)
            return song_id
        except Exception as e:
            print "Error retrieving data from " + self.get_url()
            print e

    def transform_response(self, response):
        response_json = response.json()
        search_results = response_json["response"]["hits"]
        first_result = search_results[0]["result"]
        song_id = first_result["id"]
        return song_id
