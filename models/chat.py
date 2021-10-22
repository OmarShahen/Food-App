from mongoengine import connect
from mongoengine import Document,EmbeddedDocument 
from mongoengine.fields import EmbeddedDocumentField, IntField, StringField, ListField

connect('saus')

class Messages(EmbeddedDocument):
    owner=StringField(required=True)
    to=StringField(required=True)
    text=StringField(required=True)

class Chats(Document):
    members=ListField(required=True)
    messages=ListField(EmbeddedDocumentField(Messages))


    def getMembersChat(member1, member2, chatList):
        members_chats = []
        for chat_doc in chatList:
            print(chat_doc.members)
            if (member1 in chat_doc.members) and member2 in chat_doc.members:
                members_chats.append(chat_doc)
                break
        return members_chats


