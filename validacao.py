import re


def valide(padrao='', mensagem=''):
    """Molde para criar validações genéricas
    de input com expressões regulares
    """
    resposta = input(mensagem)
    regex = re.compile(rf'{padrao}')
    busca = regex.search(resposta)
    if busca is None:
        raise ValueError
    else:
        return resposta


def valide_nascimento(mensagem=''):
    """Função específica para a validação de
    datas de nascimento e conversão para date
    do MYSQL
    """
    resposta = input(mensagem)
    regex = re.compile(r'([0-3][1-9])/([0-1][0-9])/([1-2][9|0][0-9][0-9])')
    nascimento = regex.search(resposta)
    if nascimento is None:
        raise ValueError
    else:
        return f'{nascimento.group(3)}-{nascimento.group(2)}-{nascimento.group(1)}'
