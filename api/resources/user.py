
from flask_restful import Resource
from website.module import User
from api.schemas.userSchema import UserSchema


class UserList(Resource):

    def get(self):

        users = User.query.all()
        schema = UserSchema(many=True)
        
        return {"results:":schema.dump(users)}
    
    # def post(self): doesnt required because user create his account from frontend side of app





