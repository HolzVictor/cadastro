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


def leiaNome(mensagem=''):
    resposta = input(mensagem)
    regex = re.compile(r'[a-zA-Z ]{1,30}')
    nome = regex.search(resposta)
    if nome is None or nome.group() != resposta:
        raise AttributeError('Nome inválido.')
    else:
        return resposta


def leiaSexo(mensagem=''):
    resposta = input(mensagem)
    regex = re.compile(r'M|F')
    sexo = regex.search(resposta)
    if sexo is None or sexo.group() != resposta:
        raise AttributeError('Sexo inválido.')
    else:
        return sexo


def leiaNascimento(mensagem=''):
    resposta = input(mensagem)
    regex = re.compile(r'([0-3][1-9])/([0-1][0-9])/([1-2][9|0][0-9][0-9])')
    nascimento = regex.search(resposta)
    if nascimento is None:
        raise AttributeError('Data inválida')
    else:
        return f'{nascimento.group(3)}/{nascimento.group(2)}/{nascimento.group(1)}'


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
