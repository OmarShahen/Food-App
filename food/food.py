from flask import Blueprint, jsonify, request
from models.food import Foods
from auth.verify_token import verify_user
import traceback


food_route = Blueprint('food_route', __name__)

def serialize_document_id(food_list):
    foods_data = []
    for i in range(0, len(food_list)):
        for index in food_list:
            food_dict = {}
            for key in index:
                if key == 'id':
                    food_dict[key] = str(index[key])
                else:
                    food_dict[key] = index[key]
            foods_data.append(food_dict)
    return foods_data


@food_route.route('/food/<food_name>/<int:page>', methods=['GET'])
def get_food_by_name(food_name, page):
    
    try:

        if not verify_user(request.headers.get('x-access-token')):
            return jsonify({
                'accepted': False,
                'message': 'invalid token'
            }), 406

        if page == 1:
            food_db = Foods.objects.filter(foodName__contains=food_name).limit(10)
            food_data = serialize_document_id(food_db)
            return jsonify(food_data), 200
        
        food_db = Foods.objects.filter(foodName__contains=food_name).skip((page-1)*10).limit(10)
        food_data = serialize_document_id(food_db)
        return jsonify(food_data), 200


    except Exception:
        traceback.print_exc()
        return jsonify({
            'accepted': False,
            'message': 'internal server error'
        }), 500
