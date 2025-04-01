<<<<<<< HEAD
from ProjFlask_1 import app
=======
from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormCadastro, FormLogin
from flask_sqlalchemy import SQLAlchemy
from models import Usuario


app = Flask(__name__)
app.config['SECRET_KEY'] = '1072e926d71a094f491476e564a2443f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:201611@localhost/FLASK_P1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/usuarios')
def usuarios():
    lista_usuarios = ['João', 'Maria', 'Pedro', 'Ana', 'Carlos']
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    form_login = FormLogin() #Uma instância do formulário de Login
    if form_login.validate_on_submit():
        flash('Login realizado com sucesso!', 'alert-success')
        return redirect(url_for('home')) #Após realizar o login, usuário é redirecionado para a página de login
    return render_template('login.html', form_login=form_login)

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    form_cadastro = FormCadastro()
    if form_cadastro.validate_on_submit():
        usuario = Usuario(username=form_cadastro.username.data, email=form_cadastro.email.data, senha=form_cadastro.senha.data)
        db.session.add(usuario)
        db.session.commit()
        
        flash('Cadastro efetuado com sucesso!', 'alert-success')
        return redirect(url_for('home'))
    return render_template('cadastro.html', form_cadastro=form_cadastro)

>>>>>>> 15d61f5bd699a34d62da3a6de38d04d5d6b18b67


if __name__ == '__main__':
    app.run(debug=True)


