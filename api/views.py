
from flask import Blueprint, jsonify
from flask_restful import Api
from api.resources.user import UserList
from marshmallow import ValidationError

blueprint = Blueprint("api",__name__,url_prefix="/api")

api = Api(blueprint,errors=blueprint.errorhandler)

api.add_resource(UserList,"/users")


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 404