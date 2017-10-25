from abc import ABCMeta, abstractmethod

class GeniusRequest():
    __metaclass__ = ABCMeta

    def __init__(self, access_token):
        self.base_url = "https://api.genius.com"
        self.access_token = access_token
        super(GeniusRequest, self).__init__()

    @abstractmethod
    def get_url(self):
        pass

    @abstractmethod
    def get_params(self):
        pass
