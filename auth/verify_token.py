from traceback import print_exc
from config.config import Config
from models.user import Users
import jwt
import traceback

def verify_user(access_token):
    try:
        token = jwt.decode(access_token, Config.SECRET_KEY, algorithms=['HS256'])
        if len(Users.objects(id=token['user_id'])) != 1:
            return False
        return True
    except Exception:
        traceback.print_exc()
        return False





