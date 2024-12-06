import requests
from langdetect import detect
from bs4 import BeautifulSoup


class WikiSearch:
    def __init__(self, query):
        self.query = query
        self.results = []

    def detect_language(self):
        try:
            lang = detect(self.query)
            return lang
        except:
            return 'en'

    def search(self):
        lang = self.detect_language()
        if lang == 'ru':
            URL = "https://ru.wikipedia.org/w/api.php"
        else:
            URL = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "list": "search",
            "srsearch": self.query,
            "format": "json",
            "srlimit": 10,
            "utf8": 1
        }

        answer = requests.get(URL, params=params)
        json_answer = answer.json()

        if "query" in json_answer and "search" in json_answer["query"]:
            self.results = json_answer["query"]["search"]

    def get_results(self):
        results = [
            (result["title"], self.clean_html(result["snippet"])) for result in self.results
        ]
        return results

    def clean_html(self, raw_html):
        soup = BeautifulSoup(raw_html, "html.parser")
        return soup.get_text()







