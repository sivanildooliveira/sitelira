from comunidadeimpressionadora import app
import secrets
import os




def salvar_imagem(imagen):
    #adicionar codigo aleatorio
    codigo = secrets.token_hex(8)
    nome, extencao = os.path.splitext(imagen.filename)
    nome_arquivo = nome + codigo + extencao

    #reduzir tamnho da imagem
    tamanho = (200,200)
    

    #salvar imagem no banco
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', nome_arquivo)

    #mudar campo  foto perfil

    return nome_arquivo