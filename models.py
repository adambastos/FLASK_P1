from main import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False) #nullable False diz que não pode ser null   
    email = db.Column(db.String(100), unique=True, nullable=False) 
    senha = db.Column(db.String(100), nullable=False)
    foto_perfil = db.Column(db.String, default='default.jpg')
    posts = db.relationship('Post', backref='autor', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.column(db.String, nullable=False)
    corpo = db.Column(db.Text, nullable=False)
    data_criacao = db.column(db.DateTime, nullable=False, default=lambda: datetime.utcnow())
    id_autor = db.Column(db.Interger, db.ForeignKey('usuario.id'), nullable=False) #Nesse caso, ('Usuario.id') é: NomeTabela.OCampo que é chave nela e será referência aqui em posts
    