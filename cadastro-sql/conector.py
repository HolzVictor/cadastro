import mysql.connector
from utilitarios import *
from leitores import *
from time import sleep

# Cria um objeto de conexão
con = mysql.connector.connect(host='localhost',
                              database='registros',
                              user='root',
                              password='252319',
                              autocommit=True)
# Cria um objeto de cursor
cursor = con.cursor()

# Cria a tabela de cadastro
cursor.execute('''
create table pessoas (
id int auto_increment not null,
nome varchar(30) not null,
sexo enum('M', 'F'),
nascimento date,
telefone varchar(20),
email varchar(30),
primary key (id)
) default charset = utf8;
''')


# Cadastra os registros no banco de dados
def cadastrar():
    try:
        nome = leiaNome('Nome: ')
        sexo = leiaSexo('Sexo[M/F]: ')
        nascimento = leiaNascimento('Nascimento[DD/MM/AAAA]: ')
        telefone = leiaTelefone('Telefone: ')
        email = leiaEmail('Email: ')
    except:
        print('Retornando ao menu...')
    else:
        cursor.execute(f'''
        insert into pessoas values
        (default, '{nome}', '{sexo}', '{nascimento}', '{telefone}', '{email}');
 ''')


# Lê os registros do banco de dados e mostra-os formatos na tela
def lerCadastro():
    try:
        cursor.execute('select * from pessoas;')
    except:
        print('[ERRO] Falha ao ler cadastros.')
    else:
        registros = cursor.fetchall()
        tabela(registros)


def alterar():
    cursor.execute('select * from pessoas;')
    registros = cursor.fetchall()
    print('ID    Nome')
    for registro in registros:
        print(f'[{registro[0]}]   {registro[1]}')
    try: 
        id = leiaID('Selecione um cadastro[0 para sair]: ')
    except:
        print('[ERRO] Falha ao selecionar cadastro.')
    else:
        cursor.execute(f"select * from pessoas where id='{id}'")
        cadastro = cursor.fetchall()
        tabela(cadastro)
        try:
            coluna = leiaColuna('O que você quer alterar? ')
        except:
            print('[ERRO] Insira uma coluna válida.')
        else:
            alterarRegistro(coluna, id)


def deletar():
    lista = []
    titulo('DELETAR CADASTROS')
    cursor.execute('select * from pessoas;')
    registros = cursor.fetchall()
    cursor.execute('select id from pessoas;')
    cadastros = cursor.fetchall()
    print('ID    Nome')
    for registro in registros:
        print(f'[{registro[0]}]   {registro[1]}')
    while True:
        try:
            id = leiaID('Selecione um cadastro[0 para sair]: ')
        except:
            print('[ERRO] Falha ao selecionar cadastro.')
        else:
            for cadastro in cadastros:
                for item in cadastro:
                    lista.append(item)
            if id == 0:
                titulo('Retornando ao menu...')
                sleep(2)
                break
            elif id in lista:
                try:
                    cursor.execute(f"delete from pessoas where id='{id}'")
                except:
                    print('[ERRO] Falha ao deletar cadastro.')
                else:
                    print('Cadastro deletado com sucesso.')
                    break
            else:
                print('[ERRO] Cadastro inexistente.')
