from main import db
from flask_sqlalchemy import SQLAlchemy

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(100), nullable)