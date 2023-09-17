from mongoengine import *


class Author(Document):
    fullname = StringField(max_length=50, required=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField()
    meta = {'collection': 'authors'}


class Quote(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Author)
    quote = StringField()
    meta = {'collection': 'quotes'}