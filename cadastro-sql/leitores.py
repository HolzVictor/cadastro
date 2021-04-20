import re
from utilitarios import *


def leiaInt(mensagem=''):
    resposta = input(mensagem)
    regex = re.compile(r'[1-5]')
    num = regex.search(resposta)
    if num is None or num.group() != resposta:
        raise AttributeError('Opção inválida.')
    else:
        return int(resposta)


def leiaID(mensagem=''):
    resposta = input(mensagem)
    regex = re.compile(r'[0-9]{1,3}')
    num = regex.search(resposta)
    if num is None or num.group() != resposta:
        raise AttributeError('Opção inválida.')
    else:
        return int(resposta)


def leiaColuna(mensagem=''):
    resposta = input(mensagem)
    regex = re.compile(r'(nome)|(sexo)|(nascimento)|(telefone)|(email)')
    coluna = regex.search(resposta)
    if coluna is None or coluna.group() != resposta:
        print('Coluna inválida.', end=' ')
        raise AttributeError
    else:
        return resposta


def leiaNome(mensagem=''):
    resposta = input(mensagem)
    regex = re.compile(r'[a-zA-Z ]{1,30}')
    nome = regex.search(resposta)
    if nome is None or nome.group() != resposta:
        print('Nome inválido.', end=' ')
        raise AttributeError
    else:
        return resposta


def leiaSexo(mensagem=''):
    resposta = input(mensagem)
    regex = re.compile(r'M|F')
    sexo = regex.search(resposta)
    if sexo is None or sexo.group() != resposta:
        print('Sexo inválido.', end=' ')
        raise AttributeError
    else:
        return sexo.group(0)


def leiaNascimento(mensagem=''):
    resposta = input(mensagem)
    regex = re.compile(r'([0-3][1-9])/([0-1][0-9])/([1-2][9|0][0-9][0-9])')
    nascimento = regex.search(resposta)
    if nascimento is None:
        print('Data inválida.', end=' ')
        raise AttributeError
    else:
        return f'{nascimento.group(3)}-{nascimento.group(2)}-{nascimento.group(1)}'


def leiaTelefone(mensagem=''):
    resposta = input(mensagem)
    regex = re.compile(r'''
(\(?\d{2}\)?)?
(-|\s)?
(9\s?)?
\d{4}
(-|\s)?
\d{4}
    ''', re.VERBOSE)
    telefone = regex.search(resposta)
    if telefone is None or telefone.group() != resposta:
        print('Telefone inválido.', end=' ')
        raise AttributeError
    else:
        return telefone.group(0)


def leiaEmail(mensagem=''):
    resposta = input(mensagem)
    regex = re.compile(r'''
[a-zA-Z0-9._%+-]+    # nome de usuário
@                    # símbolo @
[a-zA-Z0-9.-]+       # nome de domínio
[\.[a-zA-Z]{2,4}     # ponto alguma coisa  
''', re.VERBOSE)
    email = regex.search(resposta)
    if email is None or email.group() != resposta:
        print('Email inválido.', end=' ')
        raise AttributeError
    else:
        return email.group(0)
