from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuarios


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(message='Campo Obrigatorio *')])
    email = StringField('E-mail', validators=[DataRequired(message='Campo Obrigatorio *'), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(message='Campo Obrigatorio *'), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(message='Campo Obrigatorio *'), EqualTo('senha', message='A senha digitada não é correspodente!')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuarios.query.filter_by(email=email.data).first()

        if usuario:
            raise ValidationError(f'O e-mail "{email.data}" já está em uso.')


class FormLogin(FlaskForm):
    lemail = StringField('E-mail', validators=[DataRequired(message='Campo Obrigatorio *'), Email()])
    lsenha = PasswordField('Senha', validators=[DataRequired(message='Campo Obrigatorio *'), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')
