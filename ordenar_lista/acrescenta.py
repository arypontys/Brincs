from genericpath import exists
import os
from pathlib import Path


#função para criar e escrever em um arquivo de texto
def escrever(arg):

    # Se não existir o diretório ele deverá ser criado
    if not exists('diretorio_teste'):
        os.mkdir('diretorio_teste')

    # Entrar no diretório
    os.chdir('diretorio_teste')

    # Criar arquivo
    Path('lista.txt').touch()

    with open('lista.txt', 'r+', encoding="utf-8") as e:
        e.writelines(arg)



escrever('O que será\nque será?\n.\n')