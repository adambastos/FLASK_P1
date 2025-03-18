from main import db
from flask_sqlalchemy import SQLAlchemy

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(100), nullable=False) #nullable False diz que não pode ser null   
    email = db.column(db.String(100), unique=True, nullable=False) 
    senha = db.column(db.String(100), nullable=False)