from utilitarios import *
from leitores import *
from conector import *
from time import sleep

while True:
    menu(['Ver cadastro', 'Cadastrar pessoa', 'Atualizar cadastro', 'Deletar cadastro', 'Sair do sistema'])

    try:
        comando = leiaInt(f'Sua opção: ')
    except:
        print(f'Opção inválida.')
    else:
        if comando == 1:
            lerCadastro()
        elif comando == 2:
            cadastrar()
        elif comando == 3:
            alterar()
        elif comando == 4:
            deletar()
        elif comando == 5:
            titulo('Saindo do sistema... Até logo!')
            sleep(2)
            break
