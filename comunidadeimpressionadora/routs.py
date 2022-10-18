
from fileinput import filename
from flask import render_template, redirect, url_for, request, flash
from comunidadeimpressionadora import app, database#, bcrypt
from comunidadeimpressionadora.forms import FormCriarConta, FormLogin, FormEditarPerfil
from comunidadeimpressionadora.functionss import salvar_imagem
from comunidadeimpressionadora.models import Usuarios, Post
from flask_login import login_user, logout_user, current_user, login_required
from comunidadeimpressionadora import functionss

@app.route('/')
@login_required
def home():
    return render_template('home.html')
 

@app.route('/contato')
@login_required
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
@login_required
def usuarios():
    lista_usuarios = Usuarios.query.all()
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuarios.query.filter_by(email=form_login.lemail.data).first()     
        if usuario and  form_login.lsenha.data == usuario.senha:#bcrypt.check_password_hash(usuario.senha, form_login.lsenha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)        
            flash(f'Login feito com sucesso no e-mail: {form_login.lemail.data}', 'alert-success')        
            par_next = request.args.get('next')
            print(par_next)
            if par_next:
                return redirect(par_next)
            else:
                return redirect(url_for('home'))       	 
        else:
            flash(f'Falha no login! E-mail ou senha não confere. Tente novamente.', 'alert-danger')


    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        par_next = request.args.get('next')
        #criar usuario
        senha_criptografada = form_criarconta.senha.data#bcrypt.generate_password_hash(form_criarconta.senha.data)
        print(senha_criptografada)
        usuario = Usuarios(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_criptografada)
        #adicionar usuario a sessao
        database.session.add(usuario)
        #comitar no banco de dados
        database.session.commit()
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        usuario = Usuarios.query.filter_by(email=form_criarconta.email.data).first()
        login_user(usuario)
        if par_next:
            return redirect(par_next)
        else:
            return redirect(url_for('home'))
        
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)
    

@app.route('/sair')
def sair():
	logout_user()
	flash('Logout feito com sucesso', 'alert-warning')
	return redirect(url_for('home'))



@app.route('/perfil')
@login_required
def perfil():
    editor = False
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('perfil.html', foto_perfil=foto_perfil, editor=editor)







@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    editor = True
    form = FormEditarPerfil()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.foto_perfil.data:
            nome_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
            
        database.session.commit()
        flash('Perfil Alterado com Sucesso!', 'alert-success')
        return redirect(url_for('perfil'))
    form.username.data = current_user.username
    form.email.data = current_user.email
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('editarperfil.html', form=form,  foto_perfil=foto_perfil, editor=editor)




@app.route('/post/criar', methods=['GET', 'POST'])
@login_required
def criar_post():
	return render_template('criarpost.html')

