from uteis import *


def arquivoExiste(arquivo):
    try:
        open(arquivo, 'r')
    except FileNotFoundError:
        print(f'{vermelho()}[ERRO] Arquivo não existe.{limpa()}')
        return False
    else:
        return True


def criaArquivo(arquivo):
    try:
        open(arquivo, 'x')
    except:
        print(f'{vermelho()}[ERRO] Falha ao criar o arquivo.{limpa()}')
    else:
        print(f'{verde()}Arquivo criado com sucesso!{limpa()}')


def cadastrar(nome, idade, arquivo):
    try:
        a = open(arquivo, 'a')
    except:
        print(f'{vermelho()}[ERRO] Falha ao cadastrar o registro.{limpa()}')
    else:
        a.write(f'{nome};{idade}\n')
        print(f'{verde()}Registro {nome} adicionado com sucesso!{limpa()}')


def lerCadastro(arquivo):
        try:
            a = open(arquivo, 'r')
        except:
            print(f'{vermelho()}[ERRO] Falha ao ler o arquivo.')
        else:
            for linha in a:
                dados = linha.split(';')
                print(f'{dados[0]:<27}{dados[1]} anos'.replace('\n', ''))
