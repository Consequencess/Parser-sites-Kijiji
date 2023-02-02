import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from config.settings import options
from parsing.models import Parsing
from parsing.paginations import Paginator


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


class Parser(Paginator):
    def _get_html(self):
        driver.get(self.url)
        return driver.page_source

    def get_data(self):
        data = self._get_soup().find_all('div', class_='search-item')
        res = []
        for parser in data:
            try:
                image = parser.find('div', class_='image').img['data-src']
                added_at = '-'.join(parser.find('span', class_='date-posted').text.split('/'))
                price = parser.find('div', class_='price').text.strip()
                date = datetime.now().strftime('%m-%d-%Y')
                res.append(Parsing(image=image, price=price, added_at=added_at, date=date))
            except Exception as e:
                logging.error(f"Error while parsing data: {e}")
        Parsing.bulk_create(res)