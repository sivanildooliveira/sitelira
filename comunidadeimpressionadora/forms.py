from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuarios


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')
    
    def validate_email(self, email):
    	usuario = Usuarios.query.filter_by(email=email.data).first()
    	if usuario:
    		raise ValidationError('E-mail já Cadastrado! tente outro E-mail.')


class FormLogin(FlaskForm):
    lemail = StringField('E-mail', validators=[DataRequired(), Email()])
    lsenha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')
    
    #def validate_lemail(self, lemail):
#    	usuario = Usuarios.query.filter_by(email=lemail.data).first()
#    	if not usuario:
#    		raise ValidationError('E-mail não Cadastrado! verifique seu e-mail ou Crie um conta para continuar.')
#    	
#    def validate_lsenha(self, lsenha):
#    	
#    	d_senha = Usuarios.query.filter_by(email=self.lemail.data).first()
#    	try:
#    		senha_user = d_senha.senha
#    	except:
#    		return 
#    	
#    	if senha_user != lsenha.data:
#    		raise ValidationError('Senha incorreta!')
    	