import requests

class SearchRequest(GeniusRequest):

    def __init__(self, query, access_token):
        super(SearchRequest, self).__init__(access_token)
        self.endpoint = "/search"
        self.query = query

    def get_url(self):
        return self.base_url + self.endpoint

    def get_params(self):
        return {'query': self.query, 'access_token': self.access_token}
