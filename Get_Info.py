import webbrowser
from Console_Work import ConsoleWork
from Search import WikiSearch


class GetInfo:
    def __init__(self):
        self.searcher = None
        self.console = ConsoleWork()

    def process(self):
        query = self.console.get_query()
        self.searcher = WikiSearch(query)
        self.searcher.search()

        results = self.searcher.get_results()
        if results:
            self.console.show_results(results)
            selection = self.console.get_selection(len(results))
            title, snippet = results[selection]

            # Обработка URL для открываемой статьи
            base_url = "https://ru.wikipedia.org/wiki/" if self.searcher.detect_language() == 'ru' else "https://en.wikipedia.org/wiki/"
            article_url = f"{base_url}{title.replace(' ', '_')}"
            webbrowser.open(article_url)
        else:
            print("Статьи по вашему запросу не найдены.")




