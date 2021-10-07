from mongoengine import connect
from mongoengine import Document
from mongoengine.fields import IntField, StringField, FloatField

connect('saus')

class Foods(Document):
    NDB_No = IntField(required=True)
    foodName = StringField(required=True)
    water = FloatField(required=True)
    calorie = IntField(required=True)
    protein = FloatField(required=True)
    lipid = FloatField(required=True)
    ash = FloatField()
    carbohydrate = FloatField(required=True)
    fiber = FloatField()
    sugar = FloatField()
    calcium = IntField()
    iron = FloatField()
    magnesium = IntField()
    phosphorus = IntField()
    potassium = IntField()
    sodium = IntField()
    zinc = FloatField()
    copper = FloatField()
    manganese = FloatField()
    selenium = FloatField()
    vitaminC = FloatField()
    thiamin = FloatField()
    riboflavin = FloatField()
    niacin = FloatField()
    pantoAcid = FloatField()
    vitaminB6 = FloatField()
    folate = IntField()
    folicAcid = IntField()
    foodFolate = IntField()
    folateDFE = IntField()
    choline = FloatField()
    vitaminB12 = FloatField()
    vitaminAIU = IntField()
    vitaminARAE = IntField()
    retinol = IntField()
    alphaCarot = IntField()
    betaCarot = IntField()
    betaCrypt = IntField()
    lycopene = IntField()
    lutANDzea = IntField()
    vitaminE = FloatField()
    vitaminDUG = FloatField()
    vitaminDIU = IntField()
    vitaminK = FloatField()
    faSat = FloatField()
    faMono = FloatField()
    faPoly = FloatField()
    cholestrl = IntField()
    gmWt1 = FloatField()
    gmWtDesc1 = StringField()
    gmWt2 = FloatField()
    gmWtDesc2 = StringField()
    refusePct = IntField()






    









