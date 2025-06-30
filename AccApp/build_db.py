from flask import Flask, render_template
from controllers.build_controller import build_controller
from config import Config
from models import db

app = Flask(__name__)   


# Configure the app with the database configuration
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

app.register_blueprint(build_controller)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True) 
    # the app is also accessable from other devices in the same network 