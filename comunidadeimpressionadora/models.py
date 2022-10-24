from comunidadeimpressionadora import app, database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
	return Usuarios.query.get(int(id_usuario))

class Usuarios(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    bg_perfil = database.Column(database.String, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQY3guJ4qjDP7jDghL_R7rpNM8ERV98VwKVLw&usqp=CAU')
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='não informado')


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.String, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuarios.id'), nullable=False)



with app.app_context():

    #database.drop_all()
    #database.create_all()

    pass