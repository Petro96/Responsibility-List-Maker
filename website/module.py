
from . import db # . <=> from website import db - init package
from flask_login import UserMixin
from sqlalchemy.sql import func 
from datetime import datetime




class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30),nullable=False)
    first_name = db.Column(db.String(40), nullable=False)
    notes = db.relationship('Note', backref='notes_owner', lazy=True) # relate with Notes object


    def can_update(self, task_object):
        # return task_objcet in self.notes 
        if task_object.user_id == self.id:
            return True
        else:
            return False


    @property
    def password_hash(self):
        return self.password
    
    """ @property.setter
    def password_hash(self,password_to_hash):

        self.password = bcrypt.generate_password_hash(password_to_hash).decode('utf-8')


    def check_password_correction(self,password_to_check):
        return bcrypt.check_password_hash(self.password, password_to_check)
 """


class Note(db.Model):

    is_done = ""

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    data = db.Column(db.String(50))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # owner of notes
    #done = db.Column(db.Boolean, default=False)
    
    def set_update(self, new_task):
        self.data = new_task
        db.session.commit()

    @property
    def get_is_done(self):
        return self.is_done

    @get_is_done.setter    
    def set_is_done(self, done):
        self.is_done = done

    def __str__(self) -> str:
        return f"{self.id} - {self.data} - {self.user_id} = {self.is_done}"

    
