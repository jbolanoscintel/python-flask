from flask import request, render_template
from flask_jwt_extended import create_access_token, decode_token
from ..models import User, db
from flask_restx import Resource
import datetime

from jwt.exceptions import ExpiredSignatureError, DecodeError, \
    InvalidTokenError
from ..resources.errors import SchemaValidationError, EmailDoesnotExistsError, InternalServerError
from ..services.email_service import send_email


class ForgotPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'
        try:
            body = request.get_json()
            email = body.get('email')

            if not email:
                raise SchemaValidationError

            user = db.session.query(User).filter_by(
                email=body.get("email")).first()

            if not user:
                raise EmailDoesnotExistsError

            expires = datetime.timedelta(hours=24)
            reset_token = create_access_token(
                str(user.id), expires_delta=expires)

            return send_email('[Movie-bag] Reset Your Password',
                              sender='support@movie-bag.com',
                              recipients=[user.email],
                              text_body=render_template('email/reset_password.txt',
                                                        url=url + reset_token),
                              html_body=render_template('email/reset_password.html',
                                                        url=url + reset_token))

        except Exception as e:
            raise InternalServerError


class ResetPassword(Resource):
    def post(self):
        try:
            body = request.get_json()
            reset_token = body.get('reset_token')
            password = body.get('password')

            if not reset_token or not password:
                raise SchemaValidationError

            user_id = decode_token(reset_token)['identity']

            user = db.get_or_404(User, user_id)

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
