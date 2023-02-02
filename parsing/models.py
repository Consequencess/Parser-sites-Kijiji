from peewee import *
from config.settings import db


class Parsing(Model):
    image = TextField(null=True)
    price = CharField(max_length=88, null=True)
    added_at = CharField(max_length=255, null=True)
    date = CharField(max_length=20)

    class Meta:
        database = db


db.connect()
Parsing.create_table()
db.close()