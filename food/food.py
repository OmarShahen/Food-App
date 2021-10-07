from flask import Blueprint, jsonify, request
from models.food import Foods
import traceback


food_route = Blueprint('food_route', __name__)

def serialize_document_id(food_list):
    foods_data = []
    for food in range(0, len(food_list)):
        food_dict = {}
        for index in food_list:
            for key in index:
                if key == 'id':
                    food_dict[key] = str(index[key])
                    continue
                food_dict[key] = index[key]
        foods_data.append(food_dict)
    return foods_data


@food_route.route('/food/<food_name>', methods=['GET'])
def get_food_by_name(food_name):
    
    try:
        food_db = Foods.objects.filter(foodName__contains=food_name)
        food_data = serialize_document_id(food_db)
        return jsonify(food_data), 200

    except Exception:
        traceback.print_exc()
        return jsonify({
            'accepted': False,
            'message': 'internal server error'
        }), 500
