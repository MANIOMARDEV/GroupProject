from flask_app import app

from flask_app.controllers import users
from flask_app.controllers import repairs

if __name__=="__main__":

    app.run(host='localhost', port=5005, debug=True)