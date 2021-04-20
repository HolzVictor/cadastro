import mysql.connector
from leitores import *
import utilitarios
from time import sleep


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
    try:
        cursor.execute('select * from pessoas;')
    except:
        print('[ERRO] Falha ao ler cadastros.')
    else:
        registros = cursor.fetchall()
        utilitarios.tabela(registros)


def alterar():
    cursor.execute('select * from pessoas;')
    registros = cursor.fetchall()
    print('ID    Nome')
    for registro in registros:
        print(f'[{registro[0]}]   {registro[1]}')
    try: 
        id = leiaID('Selecione um cadastro[0 para sair]: ')
    except:
        print('[ERRO] Falha ao selecionar cadastro.')
    else:
        cursor.execute(f"select * from pessoas where id='{id}'")
        cadastro = cursor.fetchall()
        utilitarios.tabela(cadastro)
        try:
            coluna = leiaColuna('O que você quer alterar? ')
        except:
            print('[ERRO] Insira uma coluna válida.')
        else:
            utilitarios.alterarRegistro(coluna, id)


def deletar():
    lista = []
    utilitarios.titulo('DELETAR CADASTROS')
    cursor.execute('select * from pessoas;')
    registros = cursor.fetchall()
    cursor.execute('select id from pessoas;')
    cadastros = cursor.fetchall()
    print('ID    Nome')
    for registro in registros:
        print(f'[{registro[0]}]   {registro[1]}')
    while True:
        try:
            id = leiaID('Selecione um cadastro[0 para sair]: ')
        except:
            print('[ERRO] Falha ao selecionar cadastro.')
        else:
            for cadastro in cadastros:
                for item in cadastro:
                    lista.append(item)
            if id == 0:
                utilitarios.titulo('Retornando ao menu...')
                sleep(2)
                break
            elif id in lista:
                try:
                    cursor.execute(f"delete from pessoas where id='{id}'")
                except:
                    print('[ERRO] Falha ao deletar cadastro.')
                else:
                    print('Cadastro deletado com sucesso.')
                    break
            else:
                print('[ERRO] Cadastro inexistente.')
