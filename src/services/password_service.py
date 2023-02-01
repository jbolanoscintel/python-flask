from flask import request, render_template
from flask_jwt_extended import create_access_token, decode_token
from ..models import User, db
from flask_restx import Resource

from jwt.exceptions import ExpiredSignatureError, DecodeError, \
    InvalidTokenError
from ..resources.errors import SchemaValidationError, EmailDoesnotExistsError, InternalServerError
from .email_service import send_email


class ForgotPassword(Resource):
    def post():
        url = request.url + "/reset"
        try:
            body = request.get_json()
            reset_token = body.get('reset_token')
            password = body.get('password')

            if not reset_token or not password:
                raise SchemaValidationError

            user_id = decode_token(reset_token)['identity']

            user = db.get_or_404(User, id)

            user.password = password
            user.hash_password()
            db.session.commit()

            return send_email('[Movie-bag] Password reset successful',
                              sender='support@movie-bag.com',
                              recipients=[user.email],
                              text_body='Password reset was successful',
                              html_body='<p>Password reset was successful</p>')

        except SchemaValidationError:
            raise SchemaValidationError
        except EmailDoesnotExistsError:
            raise EmailDoesnotExistsError
        except Exception as e:
            raise InternalServerError
