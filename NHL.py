import requests
from config import NHL_ACCESS_KEY

class N2_API:
    def get(self, nhl_conf):
        params={'ACCESS_KEY':NHL_ACCESS_KEY}

        url= 'https://statsapi.web.nhl.com/api/v1/conferences'.format(nhl_conf)
        results = requests.get(url, params=params)
        #results = requests.get('https://statsapi.web.nhl.com/api/v1/conferences', params=params)
        return results.json()

