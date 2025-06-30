from flask import Flask, render_template
from controllers.todo_controller import todo_controller
from config import Config
from models import db


app = Flask(__name__)   

# @app.route('/')
# def hello_world():
#     names = ["John", "Jane", "Doe"]
#     return render_template("welcome.html", names=names)

# Configure the app with the database configuration
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

app.register_blueprint(todo_controller)

#load the database configuration


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True) 
    # the app is also accessable from other devices in the same network 