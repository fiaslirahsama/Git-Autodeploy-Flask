from flask import Blueprint

appindex = Blueprint('index', __name__, static_folder='static', template_folder='templates')  

from app.indexes import view