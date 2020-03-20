from peewee import *

db = PostgresqlDatabase('contacts', user='caio', password='',
                        host='localhost', port=5432)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    contact_id = AutoField(primary_key=True)
    first_name = CharField()
    last_name = CharField()
    phone_number = CharField()

# db.drop_tables([Contact])
db.create_tables([Contact])

# User runs app in the command line, initial contacts seed. User is then prompted by a few choices
# Create Contact, Look for Contact, delete contact, update contact
# If user selects Look for contact, prompted to then enter a first name, if there is a match, the contact's info is printed#

