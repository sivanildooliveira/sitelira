from comunidadeimpressionadora import app
import secrets
import os
from PIL import Image


def salvar_imagem(imagen):
    #adicionar codigo aleatorio
    codigo = secrets.token_hex(8)
    nome, extencao = os.path.splitext(imagen.filename)
    nome_arquivo = nome + codigo + extencao

    #reduzir tamnho da imagem
    tamanho = (400,400)
    imagem_reduzida = Image.open(imagen)
    imagem_reduzida.thumbnail(tamanho)

    #salvar imagem no banco
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', nome_arquivo)
    imagem_reduzida.save(caminho_completo)

    return nome_arquivo


def salvar_bg_imagem(imagem):

    #adicionar codigo aleatorio
    codigo = secrets.token_hex(8)
    nome, extencao = os.path.splitext(imagem.filename)
    nome_arquivo = nome + codigo + extencao

    #salvar imagem no banco
    caminho_completo = os.path.join(app.root_path, 'static/bg_perfil', nome_arquivo)
    imagem.save(caminho_completo)

    return nome_arquivo


def atualizar_cursos(form):
    lista_curso = []
    for campo in form:
        if "curso_" in campo.name:
            if campo.data:
                lista_curso.append(campo.label.text)
    retorno_lista = ""
    for curso in lista_curso:
        retorno_lista += f'{curso};'
    return retorno_lista[:-1]