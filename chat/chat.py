
from flask_socketio import Namespace, emit, join_room
from models.chat import Chats, Messages
from mongoengine.queryset.visitor import Q
import traceback

class user_chat(Namespace):

    def on_connect(self):
        print('User connected to user chat namespace')
    
    def on_disconnect(self):
        print('User disconnected from user chat namespace')
    
    def on_my_event(self, data):
        emit('my_response', { 'data': 'Data received successfully!' })
    
    def on_join_chat(self, data):
        join_room(data['roomID'])
    
    def on_send_message(self, data):
        try:

            # if there is no previous chat
            if data.get('roomID') == None:
                Chats(
                    members=[data['ownerID'], data['receiverID']],
                    messages=[
                        Messages(
                            owner=data['ownerID'],
                            to=data['receiverID'],
                            text=data['message']
                        )
                    ]
                ).save()

                chats = Chats.objects.filter(members__in=[data['ownerID']])
                members_chat = Chats.getMembersChat(
                    data['ownerID'],
                    data['receiverID'],
                    chats
                )
                
                data['roomID'] = str(members_chat[0].id)
                join_room(data['roomID'])
                emit('receive-message', data, to=data['roomID'])
                return 

            chat_doc = Chats.objects(id=data['roomID']).get()
            chat_doc.messages.append(Messages(
                owner=data['ownerID'],
                to=data['receiverID'],
                text=data['message']
            ))
            chat_doc.save()
            emit('receive-message', data, to=data['roomID'])
            return 
        except Exception:
            traceback.print_exc()
            emit('chat-error', {
                'message': 'there was an error please try again later'
            }, to=data['roomID'])

    
