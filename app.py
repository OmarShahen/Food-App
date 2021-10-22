from logging import debug
from flask import Flask, render_template
from flask_socketio import SocketIO
from meals.meal import meal_route
from auth.user import user_auth_bp
from food.food import food_route
from config.config import DevConfig
from chat.chat import user_chat
from users.user import user_route

app = Flask(__name__)
socketio = SocketIO(app)

app.config.from_object(DevConfig)

# Routes
app.register_blueprint(meal_route, url_prefix='/api')
app.register_blueprint(user_auth_bp, url_prefix='/api/auth')
app.register_blueprint(food_route, url_prefix='/api')
app.register_blueprint(user_route, url_prefix='/api')

# Socket 
socketio.on_namespace(user_chat('/user-chat'))




@app.route('/')
def home():
    return "Done"

@app.route('/chat-app')
def chat_app():
    return render_template('user-chat.html')



if __name__ == "__main__":
    socketio.run(app, port=5000, debug=True)