from ProjFlask_1 import db
from datetime import datetime

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(100), nullable=False) #nullable False diz que não pode ser null   
    email = db.column(db.String(100), unique=True, nullable=False) 
    senha = db.column(db.String(100), nullable=False)
    foto_perfil = db.column(db.string, default='default.png')
    posts = db.relationship('Post', backref='autor_id', lazy=True) #backref é o nome do campo que vai ser criado na tabela post para relacionar com o autor
    cursos = db.column(db.String, nullable=False, default='Não informado')
    
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    corpo = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False) 
    autor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    
