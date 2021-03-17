from utilitarios import *
from leitores import *
from time import sleep

while True:
    menu(['Ver cadastro', 'Cadastrar pessoa', 'Atualizar cadastro', 'Deletar cadastro', 'Sair do sistema'])

    try:
        comando = leiaInt(f'Sua opção: ')
    except:
        print(f'Opção inválida.')
    else:
        if comando == 1:
            print('opção 1')
        elif comando == 2:
            print('opção 2')
        elif comando == 3:
            print('opção 3')
        elif comando == 4:
            print('opção 4')
        elif comando == 5:
            titulo('Saindo do sistema... Até logo!')
            sleep(2)
            break
