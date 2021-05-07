from banco import Banco
from utilitarios import menu
from validacao import valide

db = Banco(host='localhost', user='root', password='252319')

while True:
    menu(['Ver cadastro', 'Cadastrar pessoa', 'Atualizar cadastro', 'Deletar cadastro', 'Sair do sistema'])
    try:
        opcao = int(valide(r'[1-5]', 'Sua opção: '))
    except ValueError:
        print('Selecione uma opção válida.')
    else:
        if opcao == 1:
            db.ler_registro()
        elif opcao == 2:
            db.registrar()
