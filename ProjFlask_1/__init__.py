from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '1072e926d71a094f491476e564a2443f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:201611@localhost/FLASK_P1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)