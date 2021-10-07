from flask import Flask
from meals.meal import meal_route
from auth.user import user_auth_bp
from food.food import food_route
from config.config import DevConfig

app = Flask(__name__)

app.config.from_object(DevConfig)

app.register_blueprint(meal_route, url_prefix='/api')
app.register_blueprint(user_auth_bp, url_prefix='/api/auth')
app.register_blueprint(food_route, url_prefix='/api')


@app.route('/')
def home():
    return "Done"



if __name__ == "__main__":
    app.run(debug=True, port=5000)