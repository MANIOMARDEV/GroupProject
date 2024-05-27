from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models import repair
from flask_app.models.user import User

@app.route('/new_repair')
def request_repair():
    return render_template('techrepair_create.html')

@app.route('/repair_submission', methods=['POST'])
def request_submit(): 
    if not repair.Repair.validate(request.form):
        return redirect('/new_repair')
    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'description': request.form['description'],
        'phone': request.form['phone'],  # Use get method to handle missing key
        'user_id_posted': request.form['user_id_posted'],
    }
    repair.Repair.save(data)
    return redirect('/user_dashboard')

@app.route('/delete_repair/<int:id>')
def destroy(id):
    data = {
        'id': id
    }
    repair.Repair.delete(data)
    return redirect('/user_dashboard')

@app.route('/myjobs')
def my_jobs():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_one({'id': session['user_id']})
    if not user:
        return redirect('/logout')
    return render_template('my_jobs.html', user=user, repairs=repair.Repair.get_users_jobs({'user_id_worker': session['user_id']}))

@app.route('/drop_job/<int:id>')
def drop_job(id):
    data = {
        'repair_id': id
    }
    repair.Repair.drop_job(data)
    return redirect('/myjobs')

@app.route('/become_worker', methods=['POST'])
def update_driver():
    data = {
        'repair_id': request.form['repair_id'],
        'user_id_worker': session['user_id']
    }
    repair.Repair.become_worker(data)
    return redirect('/user_dashboard')

@app.route('/detail_page/<int:id>')
def show_details(id):
    data = {
        'id': id
    }
    return render_template('view_job.html', repair=repair.Repair.get_one_with_users(data))

@app.route('/edit_job/<int:id>')
def display_edit_page(id):
    data = {
        'id': id
    }
    return render_template('edit_job.html', repair=repair.Repair.get_one_by_id(data))

@app.route('/submit_update', methods=['POST'])
def update_the_details():
    data = {
        'repair_id': request.form['repair_id'],
        'name': request.form['name'],
        'location': request.form['location'],
        'description': request.form['description'],
        'phone': request.form['phone'] # Use get method to handle missing key
    }
    repair.Repair.update(data)
    return redirect('/user_dashboard')

@app.route('/cancel_repair/<int:id>')
def worker_canceled(id):
    data = {
        'repair_id': id
    }
    repair.Repair.worker_cancel(data)
    return redirect('/user_dashboard')

@app.route('/become_worker', methods=['POST'])
def update_worker():
    data = {
        'repair_id': request.form['repair_id'],
        'user_id_worker': session['user_id']
    }
    repair.Repair.become_worker(data)
    return redirect('/user_dashboard')
