from ..RequestHandler import RequestHandler
from datetime import datetime

class MatchApi:
    ENDPOINTS = {
        'BY_MATCH_ID': '/lol/match/v5/matches/{}',
        'BY_MATCH_ID_TIMELINE': '/lol/match/v5/matches/{}/timeline',
        'BY_PUUID_MATCHLIST': '/lol/match/v5/matches/by-puuid/{}/ids'
    }

    def __init__(self, region, api_key, use_cache=True):
        self.request_handler = RequestHandler(api_key, region, True, use_cache=use_cache)

    def by_match_id(self, match_id): # Example of match_id : EUW1_6333379226
        return self.request_handler.make_request(self.ENDPOINTS['BY_MATCH_ID'].format(match_id))

    def by_match_id_timeline(self, match_id):
        return self.request_handler.make_request(self.ENDPOINTS['BY_MATCH_ID_TIMELINE'].format(match_id)) 

    def by_puuid_matchlist(
        self, 
        puuid: str,
        startTime: datetime = None,
        endTime: datetime = None,   
        queue: int = None,          # https://static.developer.riotgames.com/docs/lol/queues.json
        typeGame: str = None,       # ranked, normal, tourney, tutorial
        start: int = 0,
        count: int = 20,
    ):

        query_params = {k: v for k, v in locals().items() if v is not None and k != 'self'}

        if startTime:
            start_time = datetime.strptime(str(startTime), '%Y-%m-%d')
            start_time_seconds = int(start_time.timestamp())
            query_params['startTime'] = start_time_seconds

        if endTime:
            end_time = datetime.strptime(str(endTime), '%Y-%m-%d')
            end_time_seconds = int(end_time.timestamp())
            query_params['endTime'] = end_time_seconds

        return self.request_handler.make_request(self.ENDPOINTS['BY_PUUID_MATCHLIST'].format(puuid), query_params=query_params)