from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/usuarios')
def usuarios():
    lista_usuarios = ['João', 'Maria', 'Pedro', 'Ana', 'Carlos']
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)


