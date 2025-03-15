from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo 

class FormCadastro(FlaskForm):
    username = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)]) #Aqui diz que a senha precisa ter entre 6 até 20 caracateres
    confirm_pass = PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('senha')])
    btn_criar = SubmitField('Criar conta')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrarme = BooleanField('Lembrar meus dados')
    btn_logar = SubmitField('Entrar')