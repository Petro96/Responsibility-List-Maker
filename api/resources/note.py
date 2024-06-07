
from flask_restful import Resource
from website.module import Note
from api.schemas.noteSchema import NoteSchema
from flask import request
from extensions import db

class NoteList(Resource):

    def get(self):

        notes = Note.query.all()

        schema = NoteSchema(many=True)

        return {"results:":schema.dump(notes)}
    
    def post(self):

        schema = NoteSchema()
        
        try:
            data = schema.load(request.json)
            note = Note(data=data.data,user_id=data.user_id,done=data.done)
            db.session.add(note)
            db.session.commit()
        except ValueError as err:
            return {"Error":err.messages}
        
        return {"msg":"Note Created","note":schema.dump(note)}
    

class NoteResource(Resource):

    def get(self,note_id):
        note = Note.query.get_or_404(note_id)
        schema = NoteSchema()
        return {"note":schema.dump(note)}
    
    def put(self,note_id):

        schema = NoteSchema(partial=True)
        note = Note.query.get_or_404(note_id)

        try:
            note = schema.load(request.json,instance=note)
            db.session.add(note)
            db.session.commit()
        except ValueError as err:
            return {"Error":err.messages}
        
        return {"msg":"Note Updated","note":schema.dump(note)}
    
    def delete(self,note_id):

        note = Note.query.get_or_404(note_id)

        db.session.delete(note)
        db.session.commit()

        return {"msg":"Note Deleted"}

        

