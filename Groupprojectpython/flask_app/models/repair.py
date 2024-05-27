from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

db = 'group_project'

class Repair:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.description = data['description']
        self.phone = data['phone']
        self.user_id_posted = data['user_id_posted']
        self.user_id_worker = data['user_id_worker']

    @classmethod
    def save(cls,data):
        query = 'INSERT INTO repairs (name, location, description, phone, user_id_posted, user_id_worker, created_at, updated_at) VALUES (%(name)s, %(location)s, %(description)s, %(phone)s, %(user_id_posted)s, %(user_id_posted)s, NOW(), NOW());'
        return connectToMySQL('group_project').query_db(query,data)

    @classmethod 
    def get_one_with_users(cls,data):
        query = 'SELECT * from repairs JOIN users on user_id_posted = users.id JOIN users AS workers on user_id_worker = workers.id where repairs.id = %(id)s;'
        result = connectToMySQL('group_project').query_db(query,data)
        result = result[0]
        repair = cls(result)
        repair.posted = user.User(
            {
                'id' : result['user_id_posted'],
                'first_name' : result['first_name'],
                'last_name' : result['last_name'],
                'email' : result['email'],
                'password' : result['password']
            }
        )
        repair.worker = user.User(
            {                
                'id' : result['user_id_worker'],
                'first_name' : result['workers.first_name'],
                'last_name' : result['workers.last_name'],
                'email' : result['workers.email'],
                'password' : result['workers.password']
            }
        )
        return repair

    @staticmethod
    def validate(one_repair):
        is_valid = True
        if len(one_repair['name']) < 3:
            flash('Job Title must be three or more characters', 'danger')
            is_valid = False
        if len(one_repair['location']) < 3:
            flash('Location must be three or more characters', 'danger')
            is_valid = False
        if len(one_repair['description']) < 5:
            flash('Job Description must be 5 or more characters', 'danger')
            is_valid = False
        if len(one_repair['phone']) != 8 or not one_repair['phone'].isdigit():
            flash('Phone number must be exactly 8 digits', 'danger')
            is_valid = False
        return is_valid


# removes job from user in sessions job list
    @classmethod
    def drop_job(cls, data):
        query = 'UPDATE repairs SET user_id_worker = user_id_posted, updated_at = NOW() WHERE repairs.id = %(repair_id)s;'
        result = connectToMySQL(db).query_db(query, data)

# for the my_jobs page where it shows only the user in session's jobs that they accepted
    @classmethod
    def get_users_jobs(cls, data):
        print('running get user in sessions jobs')

        query = 'SELECT * FROM repairs JOIN users ON repairs.user_id_posted = users.id WHERE user_id_worker = %(user_id_worker)s;'

        results = connectToMySQL(db).query_db(query, data)
        print('results', results)

        repairs = []

        for row in results:
            print('iterating through results now')
            this_repair = cls(row)
            user_posted_data = {
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': '',
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at']
            }
            this_repair.posted = user.User(user_posted_data)
            repairs.append(this_repair)

            print('appending repairs with this repair:', this_repair)
            print(repairs)
        return repairs

    @classmethod
    def get_all(cls,data):
        query = 'SELECT * FROM repairs JOIN users on repairs.user_id_posted = users.id JOIN users AS workers on repairs.user_id_worker = workers.id;'
        results = connectToMySQL('group_project').query_db(query,data)
        all_repairs = []
        for row in results:
            one_repair = cls(row)
            posted_info = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password']
            }
            posted = user.User(posted_info)
            one_repair.posted = posted
            worker_info = {
                'id' : row['workers.id'],
                'first_name' : row['workers.first_name'],
                'last_name' : row['workers.last_name'],
                'email' : row['workers.email'],
                'password' : row['workers.password']
            }
            worker = user.User(worker_info)
            one_repair.worker = worker
            all_repairs.append(one_repair)
        return all_repairs

    @classmethod
    def delete(cls,data):
        query = 'DELETE from repairs Where repairs.id = %(id)s;'
        return connectToMySQL('group_project').query_db(query,data)

    @classmethod
    def become_worker(cls,data):
        query = 'UPDATE repairs SET user_id_worker = %(user_id_worker)s, updated_at = NOW() WHERE repairs.id = %(repair_id)s;'
        return connectToMySQL('group_project').query_db(query,data)

    @classmethod
    def update(cls,data):
        query = 'UPDATE repairs SET name = %(name)s, location = %(location)s, description = %(description)s, phone = %(phone)s, updated_at = NOW() WHERE repairs.id = %(repair_id)s;'
        return connectToMySQL('group_project').query_db(query,data)

    @classmethod 
    def get_one_by_id(cls,data):
        query = 'SELECT * FROM repairs Where id = %(id)s;'
        result = connectToMySQL('group_project').query_db(query,data)
        result = result[0]
        return cls(result)

    @classmethod
    def worker_cancel(cls,data):
        query = 'Update repairs SET user_id_driver = user_id_rider WHERE repairs.id = %(repair_id)s;'
        return connectToMySQL('group_project').query_db(query,data)
