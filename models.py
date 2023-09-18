from mongoengine import *


class Author(Document):
    fullname = StringField(max_length=50, required=True)
    date_born = StringField(max_length=50)
    location_born = StringField(max_length=50)
    bio = StringField()
    meta = {'collection': 'authors'}


class Quote(Document):
    keywords = ListField(StringField(max_length=30))
    author = ReferenceField(Author)
    quote = StringField()
    meta = {'collection': 'quotes'}