
from flask import Blueprint, jsonify, render_template,request, flash, get_flashed_messages
from flask_login import login_user, logout_user, login_required, current_user 
from .module import Note, User
from . import db
import json
from .form import UpdateNotes,CreateNotes, FinishedNotes, BackToTask



views = Blueprint('views', __name__) # blueprint setUp for app-flask/ blueprint create module of this file



@views.route('/welcome', methods=['GET','POST'])
def index_page():
    return render_template('index.html',user=current_user)


@views.route('/', methods=['GET','POST'])
@login_required
def home(): #notes home page

    create_task = CreateNotes()
    update_task = UpdateNotes()
    finished_task = FinishedNotes()
    back_to_task = BackToTask()

    if request.method == "POST":

        if update_task.validate_on_submit():    
        # update task

            data_for_update = request.form.get('updated_note') # data that i want to update

            update_object = Note.query.filter_by(data=data_for_update).first()

            if update_object:
                
                # user owne this note 
                if current_user.can_modify(update_object):
                    new_value = update_task.updated_data.data
                    update_object.set_update(new_value)
                    flash("Task was updated!",category="success")

            else:
                flash("Theres no Task like that in database!",category="error")

       
        #----------------------
        # create task

        if create_task.validate_on_submit():

            new_note = Note(data=create_task.note.data,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category='success')

        # ---
        # task is done 

        if finished_task.validate_on_submit():

            done_data = request.form.get('done_note') # gives note.data

            done_object = Note.query.filter_by(data=done_data).first()

            if done_object:
                # user owne this note 
                if current_user.can_modify(done_object):

                    done_object.set_is_done=True
                
                    flash("Congratulations! You've done this task.",category='success')
                else:
                    flash("Owner doesn't own the object. Object doesn't exists!",category='error')    


        # finished task back to the task
        if  back_to_task.validate_on_submit():

            done_task = request.form.get('done_task')

            done_task_object = Note.query.filter_by(data=done_task).first()

            if done_task_object:

                #is user owne this task
                if current_user.can_modify(done_task_object):

                    done_task_object.set_is_done=False

                    flash("You return your task back to Responsibilities list!",category='success')
                else:
                    flash("Owner doesn't own the object. Object doesn't exists!",category='error')
            

    # filtering data

    tasks = Note.query.filter_by(done=False)

    if tasks.count() < 1 :

        flash("Congratulations! You've done all tasks!",category='success') 

    done_tasks = Note.query.filter_by(done=True)

    if done_tasks.count() < 1:

        flash("You didn't start to do your tasks! Let's get started!",category='warning')

    return render_template("home.html",
                            user=current_user, 
                            create_task=create_task ,
                            update_task=update_task, 
                            finished_task=finished_task,
                            tasks=tasks, #return list
                            done_tasks=done_tasks, #return list
                            back_to_task=back_to_task)




@views.route('/delete-note',methods=['POST'])
def delete_note():
    # load data from request -> from js function
    note = json.loads(request.data)
    # get value from json dict
    note_id = note['note_id'] # ['key'] = value

    find_note = Note.query.get(note_id)

    if find_note:
        if current_user.can_modify(find_note):
            db.session.delete(find_note)
            db.session.commit()
            flash("Note was deleted!", category='success')
            return jsonify({
                # its called once when request is created
                "respond":"responded"
            })
        else:
            flash("There was an error about deleting note!",category='error')



