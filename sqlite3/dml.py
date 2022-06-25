"""
DML - manipulação de dados (Data Manipulation Lenguage)
Implementação de um CRUD
"""
import sqlite3


def commit_close(func):
    def decorator(*args):
        con = sqlite3.connect('sqlite3/base.db')
        cur = con.cursor()
        sql = func(*args)
        cur.execute(sql)
        con.commit()
        con.close()
    return decorator

@commit_close
def db_insert(name, phone, email):
    return """
    INSERT INTO users(name, phone, email)
        VALUES('{}', '{}', '{}')
        """.format(name, phone, email)


@commit_close
def db_update(name, email):
    return """
    UPDATE users SET name = '{}' WHERE email = '{}'
    """.format(name, email)

@commit_close
def db_delete(email):
    return """
    DELETE FROM users WHERE email='{}'
    """.format(email)


def db_select(field, data):
    con = sqlite3.connect('sqlite3/base.db')
    cur = con.cursor()
    sql = """
    SELECT id, name, phone, email
    FROM users 
    WHERE {}={}""".format(data, field)
    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data




#cur.execute(db_delete('teste@gmail.com'))
#cur.execute(db_insert('test', '84982738372', 'test@gmail.com'))
#cur.execute(db_update('teste', 'teste@gmail.com'))



