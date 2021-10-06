from traceback import print_exc
from config.config import Config
from models.user import Users
import jwt

def verify_user(access_token):
    try:
        token = jwt.decode(access_token, Config.SECRET_KEY)
        if len(Users.objects(id=token['user_id'])) != 1:
            return False
        return True
    except Exception:
        return False





