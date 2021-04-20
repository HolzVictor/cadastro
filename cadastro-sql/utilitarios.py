from conector import *
from leitores import *

def linha():
    print('-' * 35)


def titulo(mensagem):
    linha()
    print(f'{mensagem:^35}')
    linha()


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()


def coluna():
    print('''
+--------------------------------+------+------------+----------------------+------------------------------+
| Nome                           | Sexo | Nascimento | Telefone             | Email                        |
+--------------------------------+------+------------+----------------------+------------------------------+''', end='')


def tabela(registros):
    coluna()
    for registro in registros:
        print(f'''
| {registro[1]:<30} | {registro[2]:<4} | {registro[3]} | {registro[4]:<20} | {registro[5]:<28} |
+--------------------------------+------+------------+----------------------+------------------------------+''', end='')
    print('')


def alterarRegistro(coluna, id):
    if coluna == 'nome':
        try:
            nome = leiaNome('Novo nome: ')
        except:
            print('[ERRO] Nome inválido.')
        else:
            cursor.execute(f"update pessoas set nome = '{nome}' where id = '{id}'")
    elif coluna == 'sexo':
        try:
            sexo = leiaSexo('Novo sexo: ')
        except:
            print('[ERRO] Sexo inválido.')
        else:
            cursor.execute(f"update pessoas set sexo = '{sexo}' where id = '{id}'")
    elif coluna == 'nascimento':
        try:
            nascimento = leiaNascimento('Novo nascimento: ')
        except:
            print('[ERRO] Nascimento inválido.')
        else:
            cursor.execute(f"update pessoas set nascimento = '{nascimento} where id = '{id}'")
    elif coluna == 'telefone':
        try:
            telefone = leiaTelefone('Novo telefone: ')
        except:
            print('[ERRO] Telefone inválido.')
        else:
            cursor.execute(f"update pessoas set telefone = '{telefone}' where id = '{id}'")
    elif coluna == 'email':
        try:
            email = leiaEmail('Novo email: ')
        except:
            print('[ERRO] Email inválido.')
        else:
            cursor.execute(f"update pessoas set email = '{email}' where id = '{id}'")
