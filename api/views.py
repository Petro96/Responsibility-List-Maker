
from flask import Blueprint, jsonify
from flask_restful import Api
from api.resources.user import UserList, UserResource
from api.resources.note import NoteList, NoteResource
from marshmallow import ValidationError

blueprint = Blueprint("api",__name__,url_prefix="/api")

api = Api(blueprint,errors=blueprint.errorhandler)

api.add_resource(UserList,"/users")
api.add_resource(UserResource,"/users/<int:user_id>")

api.add_resource(NoteList,"/notes")
api.add_resource(NoteResource,"/notes/<int:note_id>")


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 404