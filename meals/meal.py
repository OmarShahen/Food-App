
from flask import Blueprint, request, jsonify
import traceback
from config.config import Config
from models.meal import Meals
import jwt
from auth.verify_token import verify_user


meal_route = Blueprint('meal_route', __name__)




@meal_route.route('/meals', methods=['POST'])
def create_meal():
    try:
        
        if not verify_user(request.headers.get('x-access-token')):
            return jsonify({
                'accepted': False,
                'message': 'invalid token'
            }), 406
        
        if not request.form.get('calories'):
            return jsonify({
                'accepted': False,
                'message': 'calories is a required field'
            }), 406

        if not request.form.get('category'):
            return jsonify({
                'accepted': False,
                'message': 'category is a required field'
            }), 406

        if not request.form.get('isIngredient'):
            return jsonify({
                'accepted': False,
                'message': 'isIngredient is a required field'
            }), 406
        
        if not request.form.get('isSelected'):
            return jsonify({
                'accepted': False,
                'message': 'isSelected is a required field'
            }), 406
        
        if not request.form.get('name'):
            return jsonify({
                'accepted': False,
                'message': 'name is a required field'
            }), 406
        
        if not request.form.get('recipe'):
            return jsonify({
                'accepted': False,
                'message': 'recipe field is a required field'
            }), 406
        
        if not request.form.get('servingSize'):
            return jsonify({
                'accepted': False,
                'message': 'serving size is a required field'
            }), 406 

        if not request.form.get('taken'):
            return jsonify({
                'accepted': False,
                'message': 'taken is a required field'
            }), 406
        
        if not request.form.get('unit'):
            return jsonify({
                'accepted': False,
                'message': 'unit is a required field'
            }), 406
        
        Meals(
            calories=request.form.get('calories'),
            category=request.form.get('category'),
            isIngredient=request.form.get('isIngredient'),
            isSelected=request.form.get('isSelected'),
            name=request.form.get('name'),
            recipe=request.form.get('recipe'),
            servingSize=request.form.get('servingSize'),
            taken=request.form.get('taken'),
            unit=request.form.get('unit')
        ).save()

        return jsonify({
            'accepted': True,
            'message': 'meal created successfully'
        }), 200
        

    except Exception:
        traceback.print_exc()
        return jsonify({
            'accepted': False,
            'message': 'internal server error'
        }), 500



@meal_route.route('/meals/<int:page>', methods=['GET'])
def get_meals(page):
    
    try:

        if not verify_user(request.headers.get('x-access-token')):
            return jsonify({
                'accepted': False,
                'message': 'invalid token'
            }), 406

        meals = []
        if page == 1:
            for meal in Meals.objects.limit(10):
                meals.append({
                    meal.name: {
                        'calories': meal.calories,
                        'category': meal.category,
                        'id': str(meal.id),
                        'isIngredient': meal.isIngredient,
                        'isSelected': meal.isSelected,
                        'name': meal.name,
                        'recipe': meal.recipe,
                        'servingSize': meal.servingSize,
                        'taken': meal.taken,
                        'unit': meal.unit
                    }
                })

            return jsonify(meals), 200


        for meal in Meals.objects.skip((page-1)*10).limit(10):
            meals.append({
                meal.name: {
                    'calories': meal.calories,
                    'category': meal.category,
                    'id': str(meal.id),
                    'isIngredient': meal.isIngredient,
                    'isSelected': meal.isSelected,
                    'name': meal.name,
                    'recipe': meal.recipe,
                    'servingSize': meal.servingSize,
                    'taken': meal.taken,
                    'unit': meal.unit
                }
            })
        return jsonify(meals), 200
    except Exception:
        traceback.print_exc()
        return jsonify({
            'accepted': False,
            'message': 'internal server error'
        })