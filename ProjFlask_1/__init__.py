from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '1072e926d71a094f491476e564a2443f'

from ProjFlask_1 import routes

