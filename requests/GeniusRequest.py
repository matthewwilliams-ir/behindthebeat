import abc import ABC, abstractmethod
import requests

class GeniusRequest(ABC):

    def __init__(self, access_token):
        self.base_url = "https://api.genius.com"
        self.access_token = access_token
        self.headers = {'Authorization': access_token}
        super(GeniusRequest, self).__init__()

    @abstractmethod
    def get_url(self):
        pass

    @abstractmethod
    def get_params(self):
        pass

    def execute(self):
        try:
            return response = requests.get(self.get_url(), self.get_params(), self.headers)
        except Exception as e:
            print "Error retrieving data from " + self.get_url()
            print e
