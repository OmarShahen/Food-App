from flask import Blueprint, jsonify, request, render_template
from models.user import Users
from models.chat import Chats, Messages
from utils.serialize import serialize_users_id, serialize_chats_id
from auth.verify_token import verify_user
from auth.verify_token import decode_token
from mongoengine.queryset.visitor import Q
import traceback


user_route = Blueprint('user_route', __name__)

@user_route.route('/users', methods=['GET'])
def get_all_users():

    try:

        if not verify_user(request.headers.get('x-access-token')):
            return jsonify({
                'accepted': False,
                'message': 'invalid token'
            }), 406

        users = serialize_users_id(Users.objects())

        return jsonify({
            'accepted': True,
            'message': 'Done',
            'users': users
        }), 200
    
    except Exception:
        traceback.print_exc()
        return jsonify({
            'message': 'internal server error',
            'accepted': False
        }), 500


@user_route.route('/users/contacts', methods=['GET'])
def contacts():
    try:
        users = serialize_users_id(Users.objects())

        return render_template('user-list.html', users=users)
    
    except Exception:
        traceback.print_exc()
        return jsonify({
            'message': 'internal server error',
            'accepted': False
        }), 500

@user_route.route('/users/chat/<receiver_id>', methods=['GET'])
def chat(receiver_id):

    try:
        user_id = decode_token(request.headers['x-access-token'])['user_id']
        chats = Chats.objects.filter(members__in=[user_id])
        members_chat = Chats.getMembersChat(user_id, receiver_id, chats)
        users = None

        if len(members_chat) == 0:
            print('Here in empty condition')
            Chats(
                    members=[user_id, receiver_id],
                    messages=[
                        Messages(
                            owner=user_id,
                            to=receiver_id,
                            text=''
                        )
                    ]
                ).save()
            chats = Chats.objects.filter(members__in=[user_id])
            members_chat = Chats.getMembersChat(user_id, receiver_id, chats)
            
        users = Users.objects.filter(id__in=[receiver_id, user_id]).exclude('oauth_id')
        return jsonify({
            'accepted': True,
            'chat': serialize_chats_id(members_chat),
            'users': serialize_users_id(users),
            'currentUser': user_id
        }), 200


    except Exception:
        traceback.print_exc()
        return jsonify({
            'accepted': False,
            'message': 'internal server error'
        }), 500

@user_route.route('/users/chat/no-token/<user_id>/<receiver_id>')
def chat_page(user_id, receiver_id):

    chats = Chats.objects.filter( (Q(members__in=[user_id]) and Q(members__in=[receiver_id])))
    users = Users.objects.filter(id__in=[receiver_id, user_id]).exclude('oauth_id')
    return render_template('user-chat.html', chats=serialize_chats_id(chats), users=serialize_users_id(users))

@user_route.route('/users/chat')
def chat_page_1():
    return render_template('user-chat.html')

@user_route.route('/users/search/<user_email>')
def search_users(user_email):
    try:
        
        users_db = Users.objects.filter(email__icontains=user_email)
        return jsonify({
            'accepted': True,
            'users': serialize_users_id(users_db)
        }), 200
    except Exception:
        traceback.print_exc()
        return jsonify({
            'accepted': False,
            'message': 'internal server error'
        }), 500

@user_route.route('/users/search')
def search_page():
    return render_template('search-users.html')



