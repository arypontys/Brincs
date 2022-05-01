'''
DDL - MANIPULAÇÃO DA TABELA
'''

import sqlite3

con = sqlite3.connect('sqlite3/base.db') #atribuir à variável 'con' a conecxão com o banco

cur = con.cursor() #conectar ao cursor para saber onde está dentro do banco


def db_create():
    return """
CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL)"""


cur.execute(db_create('name', 'phone', 'email')) #execuatar o comando 'sql' para criar a tabela dentro do banco
con.commit() #falar para o conector para executar o comando na basse.
con.close() # e agora precisa fechar a conexão
