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
    tamanho = (200,200)
    imagem_reduzida = Image.open(imagen)
    imagem_reduzida.thumbnail(tamanho)

    #salvar imagem no banco
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', nome_arquivo)
    imagem_reduzida.save(caminho_completo)

    return nome_arquivo