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
    cursor.execute('select * from pessoas;')
    registros = cursor.fetchall()
    for registro in registros:
        titulo('PESSOAS CADASTRADAS')
        print(f'Nome: {registro[1]}')
        print(f'Sexo: {registro[2]}')
        print(f'Nascimento: {registro[3]}')
        print(f'Telefone: {registro[4]}')
        print(f'Email: {registro[5]}')
        linha()


def deletar():
    titulo('DELETAR CADASTROS')
    cursor.execute('select * from pessoas;')
    registros = cursor.fetchall()
    for registro in registros:
        print('ID    Nome')
        print(f'[{registro[0]}]   {registro[1]}')
