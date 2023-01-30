from ..models import db
from ..models import Todo
from ..models import User
from flask_jwt_extended import create_access_token
import datetime


def create_user(body):
    try:
        user = User(**body)
        user.hash_password()
        db.session.add(user)
        db.session.commit()
        return {'user': user}, 200
    except Exception as e:
        return {'Error': e}, 500


def get_users():
    try:
        users = User.query.all()
        result = []
        for u in users:
            result.append(u.serialize())
        return result
    except Exception as e:
        return {'Error': e}, 500


def update_user(id, user_data):
    try:
        user = db.get_or_404(User, id)
        user = user_data
        db.session.commit()
        return {'user': user}, 200
    except Exception as e:
        return {'Error': e}, 500


def get_user(id):
    try:
        user = db.get_or_404(User, id)
        return {'user': user}, 200
    except Exception as e:
        return {'Error': e}, 500


def delete_user(id):
    try:
        user = db.get_or_404(User, id)
        user.active = False
        db.session.commit()
        return {'user': user}, 200
    except Exception as e:
        return {'Error': e}, 500


def activate_user(id):
    try:
        user = db.get_or_404(User, id)
        user.active = True
        db.session.commit()
        return {'user': user}, 200
    except Exception as e:
        return {'Error': e}, 500


def login(body):
    user = db.session.query(User).filter_by(
        email=body.get("email")).first()
    if user:
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Incorrect Email or Password'}, 401
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(
            identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200
    return {'error': 'Incorrect Email or Password'}, 401
