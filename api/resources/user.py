
from flask import request
from flask_restful import Resource
from website.module import User
from api.schemas.userSchema import UserSchema
from extensions import db


class UserList(Resource):

    def get(self):

        users = User.query.all()
        schema = UserSchema(many=True)
        
        return {"results:":schema.dump(users)}
    
    # def post(self): doesnt required because user create his account from frontend side of app

class UserResource(Resource):

    def get(self,user_id):
        user = User.query.get_or_404(user_id)

        schema = UserSchema()

        return {"user":schema.dump(user)}
    
    def put(self,user_id):
        user = User.query.get_or_404(user_id)

        schema = UserSchema(partial=True)

        user = schema.load(request.json, instance=user)

        db.session.add(user)
        db.session.commit()

        return {"msg":"User updated", "user":schema.dump(user)}
    
    def delete(self,user_id):
        user = User.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()

        return {"msg":"User deleted"}



