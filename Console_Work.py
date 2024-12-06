class ConsoleWork:
    def get_query(self):
        return input("Введите поисковый запрос в Wikipedia:")

    def show_results(self, results):
        print("Найденные статьи:")
        for i, (title, snippet) in enumerate(results):
            print(f"{i + 1}: {title} - {snippet}")

    def get_selection(self, max_selection):
        while True:
            try:
                selection = int(input(f"Выберите номер статьи (1-{max_selection}): "))
                if 1 <= selection <= max_selection:
                    return selection - 1
                else:
                    print(f"Пожалуйста, выберите номер от 1 до {max_selection}.")
            except ValueError:
                print("Пожалуйста, введите действительный номер.")