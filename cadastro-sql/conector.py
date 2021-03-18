import mysql.connector
from leitores import *

con = mysql.connector.connect(host='localhost', database='registros', user='root', password='252319', autocommit=True)
cursor = con.cursor()


def cadastrar():
    try:
        nome = leiaNome('Nome: ')
        sexo = leiaSexo('Sexo[M/F]: ')
        nascimento = leiaNascimento('Nascimento[DD/MM/AAAA]: ')
        telefone = leiaTelefone('Telefone: ')
        email = leiaEmail('Email: ')
    except:
        print('Retornando ao menu...')
    else:
        cursor.execute(f'''
        insert into pessoas values
        (default, '{nome}', '{sexo}', '{nascimento}', '{telefone}', '{email}');
 ''')


def lerCadastro():
    cursor.execute('select count(*) from pessoas;')
    tamanho = len(cursor.fetchall())
    for i in range(tamanho):
        cursor.execute('select * from pessoas;')
        print(cursor.fetchall())
