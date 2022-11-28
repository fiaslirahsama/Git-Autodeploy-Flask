import os, pymysql
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists,create_database
# linux to windows

# set the base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Auto Create Name DB
def validateDatabase(DATABASE_FILE, DB_NAME):
    engine = create_engine(DATABASE_FILE)
    if not database_exists(engine.url): # Checks for the first time  
        create_database(engine.url)     # Create new DB    
        print(f"{DB_NAME} Database Created") # Verifies if database is there or not.
    else:
        print(f"Database {DB_NAME} Running")

# Create the super class
class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY')
  # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
  # SQLALCHEMY_TRACK_MODIFICATIONS = False
  
  
# Create the development config
class DevelopmentConfig(Config):
  DEBUG = True
  # SQLALCHEMY_DATABASE_URI = 'mysql:///'+os.path.join(basedir, 'coba_db.db') #TODO
   
  
  # HOST = str(os.environ.get("DB_HOST"))
  # DATABASE = str(os.environ.get("DB_DATABASE"))
  # USERNAME = str(os.environ.get("DB_USERNAME"))
  # PASSWORD = str(os.environ.get("DB_PASSWORD"))
  
  # DATABASE_FILE = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
  
  # # TODO Testing multiple database
  # SQLALCHEMY_BINDS = {
  #       'db2': 'mysql://mtn:mtnok@192.20.143.79/IOT_KL'
  # }
  
  # validateDatabase(DATABASE_FILE, DATABASE)
  # # SQLALCHEMY_DATABASE_URI = DATABASE_FILE
  # # SQLALCHEMY_TRACK_MODIFICATIONS = False
  # # SQLALCHEMY_RECORD_QUERIES = True 
  

  # secret_key_mysql = 'inipassword' # untuk proteksi extra

  # host_mysql = ['MYSQL_HOST']='192.168.5.171'  # dikoneksikan dengan database
  # username_mysql = ['MYSQL_USER']='admin'
  # password_mysql = ['MYSQL_PASSWORD']='666666'
  # database_mysql = ['MYSQL_DB']='ubs_univ'