import json
import requests


ENDPOINT = 'http://www.omdbapi.com/?apikey=e4fbd650'
RESULTS_ON_PAGE = 10


class APICall:
    def __init__(self, search, page=1):
        self.search = search
        try:
            self.page = int(page)
        except ValueError:
            pass
        self.endpoint = ENDPOINT
        self._append_param_to_url(s=self.search, page=self.page)
        self._make_call()

    def _append_param_to_url(self, **params):
        for param, value in params.items():
            self.endpoint = '{url}&{param}={value}'.format(
                url=self.endpoint,
                param=param,
                value=value
            )

    def _make_call(self):
        self.r = requests.get(self.endpoint)
        self.response = False
        content = self.r.content
        if content:
            self.data = json.loads(content)
            if 'Response' in self.data and self.data['Response'] == 'True':
                self.response = True

    def get_results(self):
        return self.data['Search'] if self.response else []

    def get_next_page(self):
        if self.response:
            total_results = int(self.data.get('totalResults', 0))
            return self.page + 1 if total_results - self.page * RESULTS_ON_PAGE > 0 else None
