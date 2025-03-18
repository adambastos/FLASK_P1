from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormCadastro, FormLogin

app = Flask(__name__)
app.config['SECRET_KEY'] = '1072e926d71a094f491476e564a2443f'

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

<<<<<<< HEAD
@app.route('/login', methods=['POST', 'GET'])
=======
@app.route('/login', methods=['GET', 'POST'])
>>>>>>> 65f71c4fa2015b2dd1c026de1292f288d3ad70b5
def login():
    form_login = FormLogin() #Uma instância do formulário de Login
    if form_login.validate_on_submit():
        flash('Login realizado com sucesso!', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login)

<<<<<<< HEAD
@app.route('/cadastro', methods=['POST', 'GET'])
=======
@app.route('/cadastro', methods=['GET', 'POST'])
>>>>>>> 65f71c4fa2015b2dd1c026de1292f288d3ad70b5
def cadastro():
    form_cadastro = FormCadastro()
    if form_cadastro.validate_on_submit():
        flash('Cadastro efetuado com sucesso!', 'alert-success')
        return redirect(url_for('home'))
    return render_template('cadastro.html', form_cadastro=form_cadastro)



if __name__ == '__main__':
    app.run(debug=True)


