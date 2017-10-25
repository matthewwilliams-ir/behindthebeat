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
            return requests.get(self.get_url(), self.get_params())
        except Exception as e:
            print "Error retrieving data from " + self.get_url()
            print e
