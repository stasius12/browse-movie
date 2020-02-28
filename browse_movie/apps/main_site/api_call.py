import json
import requests


ENDPOINT = 'http://www.omdbapi.com/?apikey=e4fbd650'


class APICall:
    def __init__(self, search):
        self.search = search
        self.endpoint = ENDPOINT
        self._append_param_to_url('s', self.search)
        self._make_call()

    def _append_param_to_url(self, param, value):
        self.endpoint = '{url}&{param}={value}'.format(
            url=self.endpoint,
            param=param,
            value=value
        )

    def _make_call(self):
        self.r = requests.get(self.endpoint)
        content = self.r.content
        if content:
            self.data = json.loads(content)

    def get_data(self):
        return self.data['Search']
