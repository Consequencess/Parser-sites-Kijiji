from decouple import config
from fake_useragent import UserAgent
from peewee import PostgresqlDatabase
from selenium import webdriver

options = webdriver.ChromeOptions()
ua = UserAgent()
options.add_argument('--headless')
options.add_argument('--disable-blink-features=AutomationControlled')


db = PostgresqlDatabase(
    database=config('DB_NAME'),
    user=config('DB_USER'),
    password=config('DB_PASSWORD'),
    host=config('DB_HOST'),
    port=config('DB_PORT')
)