from ..RequestHandler import RequestHandler
from datetime import datetime

class LolStatusApi:
    ENDPOINTS = {
        'BY_REGION': '/lol/status/v4/platform-data'
    }

    def __init__(self, region, api_key, use_cache=True):
        self.request_handler = RequestHandler(api_key, region, False, use_cache=use_cache)

    def region(self):
        return self.request_handler.make_request(self.ENDPOINTS['BY_REGION'])
    