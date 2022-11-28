from flask import Flask, url_for, render_template, session, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig
from flask_login import LoginManager, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from datetime import timedelta
from os.path import join, dirname, realpath

def center_app(config=DevelopmentConfig):  
  
    app = Flask(__name__)
    app.config.from_object(config)
    app.config["DEBUG"] = True   
    
    from app.indexes import appindex as idxx
    app.register_blueprint(idxx)
    #############################################
    ################### DASH ####################
    #############################################
    print('mlaku')
    # with app.app_context():
    #   # Import parts of our core Flask app
    #   from app_center.process.dashboard import view_dashboard

    #   # Import Dash application
    #   from app_center.process.dashboard.plotlydash.dashboard import init_dashboard
    #   app = init_dashboard(app)

      # return app
    return app