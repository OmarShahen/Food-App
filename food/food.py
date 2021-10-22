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
                elif index[key] == None:
                    continue
                else:
                    food_dict[key] = index[key]
            foods_data.append(food_dict)
    return foods_data

def search_result_optimizer(list, target):
    results = []
    exact_results = []

    print(target)

    for i in range(0, len(list)):
        for index in list:
            if target == index['foodName']:
                dict_obj = {}
                for key in index:
                    dict_obj[key] = index[key]
                exact_results.append(dict_obj)
        
    print(exact_results)
    print('Done')
    

@food_route.route('/food/<food_name>/<int:page>', methods=['GET'])
def get_foods_by_name(food_name, page):
    
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

@food_route.route('/food/<food_name>', methods=['GET'])
def get_food_by_name(food_name):
    try:
        
        if not verify_user(request.headers.get('x-access-token')):
            return jsonify({
                'accepted': False,
                'message': 'invalid token'
            }), 406
        
        food_db = Foods.objects.filter(foodName__iexact=food_name)
        search_result_optimizer(food_db, food_name)
        food_data = serialize_document_id(food_db)
        return jsonify(food_data), 200

    except Exception:
        traceback.print_exc()
        return jsonify({
            'accepted': False,
            'message': 'internal server error'
        }), 500

    