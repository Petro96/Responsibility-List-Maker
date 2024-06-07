
from extensions import ma
from website.module import Note
from marshmallow.fields import Integer,String, DateTime, Boolean
from marshmallow import validate, validates_schema , ValidationError

class NoteSchema(ma.SQLAlchemyAutoSchema):

    user_id = Integer(strict=True)

    data = String(required=False, validate=[validate.Length(min=3,max=50)], error_messages={
        'invalid':"Data is invalid, needs to be a string"
    })

    date = DateTime()

    done = Boolean()


    class Meta:

        model = Note
        load_instance = True