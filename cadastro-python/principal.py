from uteis import *
from arquivos import *
from time import sleep

arquivo = 'cadastros.txt'

if not arquivoExiste(arquivo):
    criaArquivo(arquivo)

while True:
    menu(['Ver cadastros', 'Cadastrar pessoa', 'Sair do sistema'])
    comando = int(input(f'{verde()}Sua opção:{limpa()} '))

    if comando == 1:
        titulo('PESSOAS CADASTRADAS')
        lerCadastro(arquivo)
    elif comando == 2:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastrar(nome, idade, arquivo)
    elif comando == 3:
        titulo('Saindo do sistema... Até logo!')
        sleep(2)
        break
