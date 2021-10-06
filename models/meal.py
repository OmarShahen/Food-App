from mongoengine import connect
from mongoengine import Document
from mongoengine.fields import IntField, StringField, FloatField, BooleanField

connect('saus')

class Meals(Document):
    calories = FloatField(required=True)
    category = StringField(required=True)
    image = StringField()
    isIngredient = BooleanField(required=True)
    isSelected = BooleanField()
    name = StringField(required = True)
    recipe = StringField()
    servingSize = FloatField(required=True)
    taken = IntField(required=True)
    unit = IntField(required=True)