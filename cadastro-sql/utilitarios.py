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
