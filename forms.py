from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
<<<<<<< HEAD
from wtforms.validators import DataRequired, Length, Email, EqualTo
=======
from wtforms.validators import DataRequired, Length, Email, EqualTo 
>>>>>>> 65f71c4fa2015b2dd1c026de1292f288d3ad70b5

class FormCadastro(FlaskForm):
    username = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)]) #Aqui diz que a senha precisa ter entre 6 até 20 caracateres
    confirm_pass = PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('senha')])
    btn_criar = SubmitField('Criar conta')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
<<<<<<< HEAD
    lembrar_dados = BooleanField('Lembrar dados')
=======
    lembrarme = BooleanField('Lembrar meus dados')
>>>>>>> 65f71c4fa2015b2dd1c026de1292f288d3ad70b5
    btn_logar = SubmitField('Entrar')