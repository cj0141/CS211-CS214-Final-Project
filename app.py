from flask import Flask # Imports Flask framework
from models import db   # Imports the database (models.py)
from routes import main # Imports the 'main' blueprint (routes.py)

class Config:
    SECRET_KEY = 'group1_secret_key'        # Secret key for session management and security
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/clinic_db'       # Connecting database
    SQLALCHEMY_TRACK_MODIFICATIONS = False      # Disables a feature that signals the app every time a change is made to the DB


def create_app():
    app = Flask(__name__)       # Initializes the Flask application
    
    app.config.from_object(Config)      # Loads configuration from the Config class

    db.init_app(app)       # Initializes the database with the Flask app

    app.register_blueprint(main)        # Registers the blueprint to enable the routes defined in routes.py

    with app.app_context(): 
        db.create_all()    # Creates all database tables defined in the models if they don't exist yet

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)