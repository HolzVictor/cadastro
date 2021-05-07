def linha():
    """Imprime uma linha com 35 caracteres na tela"""
    print('-' * 35)


def titulo(mensagem):
    """Imprime um título centralizado entre 35 caracteres na tela"""
    linha()
    print(f'{mensagem:^35}')
    linha()


def menu(lista):
    """Imprime um menu interativo formatado na tela"""
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()


def coluna():
    print('''
+----+--------------------------------+------+------------+----------------------+------------------------------+
| Id | Nome                           | Sexo | Nascimento | Telefone             | Email                        |
+----+--------------------------------+------+------------+----------------------+------------------------------+''', end='')


def tabela(registros):
    coluna()
    for registro in registros:
        print(f'''
| {registro[0]:<2} | {registro[1]:<30} | {registro[2]:<4} | {registro[3]} | {registro[4]:<20} | {registro[5]:<28} |
+----+--------------------------------+------+------------+----------------------+------------------------------+''', end='')
    print('')
