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
