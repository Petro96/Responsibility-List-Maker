from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired, Length


class CreateNotes(FlaskForm):

    note = StringField(validators=[Length(min=2,max=50), DataRequired()])
    submit = SubmitField(label="Add Task")



class UpdateNotes(FlaskForm):

    updated_data = StringField(label="Update Task", validators=[Length(min=2,max=60)])
    submit = SubmitField(label='Update')


class FinishedNotes(FlaskForm):

    submit = SubmitField(label="Its Done")