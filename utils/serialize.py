
from mongoengine.connection import connect


def serialize_users_id(users_list):
    serialized_users_list = []
    for i in range(0, len(users_list)):
        user_record = {}
        for key in users_list[i]:
            if key == 'id':
                user_record['id'] = str(users_list[i][key])
            else:
                user_record[key] = users_list[i][key]
        serialized_users_list.append(user_record)
    return serialized_users_list

    
def serialize_chats_id(chat_list):
    chats_list = []

    for chat in chat_list:
        chat_doc = {}
        for chat_key in chat:
            if chat_key == 'id':
                chat_doc[chat_key] = str(chat[chat_key])
                continue
            if chat_key == 'messages':
                chat_doc[chat_key] = serialize_messages_id(chat[chat_key])
            else:
                chat_doc[chat_key] = chat[chat_key]
        chats_list.append(chat_doc)
    return chats_list


def serialize_messages_id(message_list):
    messages_list = []
    for message in message_list:
        message_doc = {}
        for key in message:
            message_doc[key] = str(message[key])
        messages_list.append(message_doc)
    return messages_list

