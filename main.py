from flask import Flask, render_template, url_for
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    return render_template('login.html', form_login=form_login)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form_cadastro = FormCadastro()
    return render_template('cadastro.html', form_cadastro=form_cadastro)



if __name__ == '__main__':
    app.run(debug=True)


