
from flask import render_template, redirect, url_for, request, flash
from comunidadeimpressionadora import app, database, bcript
from comunidadeimpressionadora.forms import FormCriarConta, FormLogin
from comunidadeimpressionadora.models import Usuarios, Post



lista_usuarios = ['Lira', 'João', 'Alon', 'Alessandra', 'Amanda']

@app.route('/')
def home():
    return render_template('home.html')
 

@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    LC = 'l' if 'botao_submit_login' in request.form else 'c'

    if form_login.validate_on_submit() and LC:
        flash(f'Login feito com sucesso no e-mail: {form_login.lemail.data}', 'alert-success')
        return redirect(url_for('home'))


    if form_criarconta.validate_on_submit() and not LC:
        #criar usuario
        senha_criptografada = bcript.generate_password_hash(form_criarconta.senha.data)
        print(senha_criptografada)
        usuario = Usuarios(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_criptografada)
        #adicionar usuario a sessao
        database.session.add(usuario)
        #comitar no banco de dados
        database.session.commit()


        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'), LC=LC)

    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)