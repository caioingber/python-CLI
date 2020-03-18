from peewee import *

db = PostgresqlDatabase('contacts', user='caio', password='',
                        host='localhost', port=5432)
db.connect()