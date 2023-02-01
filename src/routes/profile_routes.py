from flask_restx import Resource
from flask_jwt_extended import jwt_required
from ..services.image_service import image_service


class ProfileApi(Resource):
    @jwt_required
    def get():
        img = ""
        return {"image": img}, 200
