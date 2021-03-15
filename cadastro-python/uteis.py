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
        print(f'{amarelo()}{c}{limpa()} - {azul()}{item}{limpa()}')
        c += 1
    linha()


def vermelho():
    return '\033[31m'


def verde():
    return '\033[32m'


def amarelo():
    return '\033[33m'


def azul():
    return '\033[34m'


def limpa():
    return '\033[m'
