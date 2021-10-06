
from flask import Blueprint, request, jsonify
from mongoengine.fields import FloatField
from models.user import Users
from config.config import Config
import traceback
import jwt

user_auth_bp = Blueprint('user_auth_bp', __name__)



@user_auth_bp.route('/users', methods=['POST'])
def create_user():

    try:
        
        if not request.form.get('from'):
            return jsonify({
                'accepted': False,
                'message': 'Oauth provider is a required field'
            }), 406
        
        if not request.form.get('name'):
            return jsonify({
                'accepted': False,
                'message': 'name is a required field'

            }), 406
        
        if not request.form.get('id'):
            return jsonify({
                'accepted': False,
                'message': 'oauth id is a required field'
            }), 406
        
        if not request.form.get('email'):
            return jsonify({
                'accepted': False,
                'message': 'email is a required field'
            }), 406

        user_data = Users.objects(email=request.form.get('email'))
        if len(user_data) != 0:
            return jsonify({
                'accepted': False,
                'message': 'this email is already taken'
            }), 406

        Users(
            oauthProvider=request.form.get('from'),
            name=request.form.get('name'),
            oauth_id=request.form.get('id'),
            email=request.form.get('email')
        ).save()

        user_data = Users.objects(email=request.form.get('email'))
        access_token = jwt.encode({'user_id': str(user_data[0].id)}, Config.SECRET_KEY).decode()

        return jsonify({
            'accepted': True,
            'message': 'account created successfully',
            'access_token': access_token
        }), 200

    except Exception:
        traceback.print_exc()
        return jsonify({
            'accepted': False,
            'message': 'internal server error'
        })


@user_auth_bp.route('/users/login', methods=['POST'])
def login_user():
    try:
        
       user_data = Users.objects(email=request.form.get('email'))
       if len(user_data) == 0:
           return jsonify({
               'accepted': False,
               'message': 'this email does not exist'
           }), 406
        
       if user_data[0]['oauth_id'] != request.form.get('id'):
            return jsonify({
                'accepted': False,
                'message': 'invalid credentials'
            }), 406

       access_token = jwt.encode({'user_id': str(user_data[0].id)}, Config.SECRET_KEY).decode()
       
       return jsonify({
           'accepted': True,
           'message': 'login successfully',
           'access_token': access_token
       }), 200


    except Exception:
        traceback.print_exc()
        return jsonify({
            'accepted': False,
            'message': 'internal server error'
        }), 500