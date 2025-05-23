from flask import Flask, render_template, url_for, request, flash, redirect
from ProjFlask_1 import app, db
from ProjFlask_1.forms import FormCadastro, FormLogin
from ProjFlask_1.models import Usuario, Post

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
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login)

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    form_cadastro = FormCadastro()
    if form_cadastro.validate_on_submit():
        usuario = Usuario(username=form_cadastro.username.data, email=form_cadastro.email.data, senha=form_cadastro.senha.data)
        db.session.add()
        db.session.commit()
        flash('Cadastro efetuado com sucesso!', 'alert-success')
        return redirect(url_for('home'))
    return render_template('cadastro.html', form_cadastro=form_cadastro)

