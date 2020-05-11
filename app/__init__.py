from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
def create_app(config_name):
    #INitializing Application
    app=Flask(__name__)

    # creating the application configurations
    app.config.from_object(config_options[config_name])
    
    # Initializing flask extensions
    db.init_app(app)
    #REGISTERING THE BLUEPRINT
       #main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
        # auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')
    
    return app