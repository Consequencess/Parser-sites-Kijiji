from config.utils import RequestTranslator


class Paginator(RequestTranslator):
    def find_button_next(self):
        pagination = self._get_soup().find('div', class_='pagination')
        return 'Next' in pagination.text