import mysql.connector
from leitores import leiaID, leiaNome, leiaSexo, leiaNascimento, leiaTelefone, leiaEmail, leiaColuna
from utilitarios import tabela, coluna, titulo
from time import sleep
from os import system

con = mysql.connector.connect(host='localhost', database='registros', user'root', password='252319')


def cadastrar():
    system('cls')
    titulo('SISTEMA DE CADASTRO')
    try:
        nome = leiaNome('Nome: ')
        sexo = leiaSexo('Sexo[M/F]: ')
        nascimento = leiaNascimento('Nascimento[DD/MM/AAAA]: ')
        telefone = leiaTelefone('Telefone: ')
        email = leiaEmail('Email: ')
    except:
        system('cls')
        sleep(1)
        titulo('Retornando ao menu...')
        sleep(2)
    else:
        cursor.execute(f'''
        insert into pessoas values
        (default, '{nome}', '{sexo}', '{nascimento}', '{telefone}', '{email}');
 ''')


# Lê os registros do banco de dados e mostra-os formatos na tela
def lerCadastro():
    try:
        cursor.execute('select * from pessoas;')
    except:
        print('[ERRO] Falha ao ler cadastros.')
    else:
        registros = cursor.fetchall()
        tabela(registros)


def alterarRegistro(coluna, id):
    if coluna == 'nome':
        try:
            nome = leiaNome('Novo nome: ')
        except:
            print('')
        else:
            cursor.execute(f"update pessoas set nome = '{nome}' where id = '{id}'")
    elif coluna == 'sexo':
        try:
            sexo = leiaSexo('Novo sexo: ')
        except:
            print('')
        else:
            cursor.execute(f"update pessoas set sexo = '{sexo}' where id = '{id}'")
    elif coluna == 'nascimento':
        try:
            nascimento = leiaNascimento('Novo nascimento: ')
        except:
            print('')
        else:
            cursor.execute(f"update pessoas set nascimento = '{nascimento}' where id = '{id}'")
    elif coluna == 'telefone':
        try:
            telefone = leiaTelefone('Novo telefone: ')
        except:
            print('')
        else:
            cursor.execute(f"update pessoas set telefone = '{telefone}' where id = '{id}'")
    elif coluna == 'email':
        try:
            email = leiaEmail('Novo email: ')
        except:
            print('')
        else:
            cursor.execute(f"update pessoas set email = '{email}' where id = '{id}'")


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
        tabela(cadastro)
        try:
            coluna = leiaColuna('O que você quer alterar? ')
        except:
            print('[ERRO] Insira uma coluna válida.')
        else:
            alterarRegistro(coluna, id)


def deletar():
    lista = []
    titulo('DELETAR CADASTROS')
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
                titulo('Retornando ao menu...')
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
