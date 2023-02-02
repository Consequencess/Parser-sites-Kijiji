import requests
from bs4 import BeautifulSoup as bs

headers = {
    "User-Agent": "?",
    "accept": "?",
    "accept-encoding": "?",
    "accept-language": "?"
}


class RequestTranslator:
    def __init__(self, url):
        self.url = url

    def _get_html(self):
        try:
            request = requests.get(url=self.url, headers=headers)
            request.raise_for_status()
            return request.text
        except requests.exceptions.RequestException as e:
            print(f"Request to {self.url} failed: {e}")
            return ""

    def _get_soup(self):
        soup = bs(self._get_html(), 'lxml')
        return soup