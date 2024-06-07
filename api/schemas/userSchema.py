
from marshmallow import validate, validates_schema ,ValidationError
from marshmallow.fields import String, Email
from extensions import ma

from website.module import User


class UserSchema(ma.SQLAlchemyAutoSchema):

    name = String(required=False,validate=[validate.Length(min=3)],error_messages={
        'invalid':"The name is invalid, needs to be a string"
    })

    email = String(required=False,validate=[validate.Email()])

    @validates_schema
    def validate_email(self, data, **kwargs):
        email = data.get("email")
        if User.query.filter_by(email=email).count():
            raise ValidationError(f"Email {email} already exists.")



    class Meta:

        model = User
        exclude = ['password']
        load_instance = True