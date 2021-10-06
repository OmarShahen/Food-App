from enum import unique
from mongoengine import connect
from mongoengine import Document
from mongoengine.fields import StringField

connect('saus')

class Users(Document):
    oauthProvider = StringField(required=True)
    token = StringField()
    name = StringField(required=True)
    oauth_id = StringField(required=True)
    email = StringField(required=True, unique=True)