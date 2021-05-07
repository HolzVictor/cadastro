import mysql.connector.errors
from mysql.connector import connect
from validacao import valide, valide_nascimento
from utilitarios import titulo, tabela


class Banco:
    """Executa operções básicas de manipukação sobre
    os registros de um banco de dados MYSQL
    """
    def __init__(self, host, user, password, database='', autocommit=True):
        """Passa os parâmetros de conexão do servidor MYSQL
        e retorna um objeto de conexão e um cursor

        Cria um banco de dados e uma tabela, caso não existam
        """
        try:
            self.con = connect(host=host, database='registros', user=user, password=password, autocommit=autocommit)
            self.cursor = self.con.cursor()
        except mysql.connector.errors.ProgrammingError:
            self.con = connect(host=host, user=user, password=password, autocommit=autocommit)
            self.cursor = self.con.cursor()
            self.cursor.execute('''create database registros
                                   default character set utf8
                                   default collate utf8_general_ci;''')

        finally:
            self.cursor.execute('use registros;')
            self.cursor.execute('show tables;')
            if self.cursor.fetchone() is None:
                self.cursor.execute('''create table pessoas(
                                       id int auto_increment not null,
                                       nome varchar(30) not null,
                                       sexo enum('M', 'F'),
                                       nascimento date,
                                       telefone varchar(20),
                                       email varchar(30),
                                       primary key (id)
                                       ) default charset = utf8;''')

    def execute(self, comando='', fetchall=False, fetchone=False):
        """Executa um comando no cursor do banco de dados
        e retorna um fetchone ou fetchall
        """
        self.cursor.execute(comando)

        if fetchall and fetchone:
            print('[ERRO] Selecione apenas um parâmetro.')
        elif fetchall:
            return self.cursor.fetchall()
        elif fetchone:
            return self.cursor.fetchone()
    
    def ler_registro(self):
        """Lê os registros da tabela e os imprime na tela tabelados"""

        self.registros = self.execute('select * from pessoas;', fetchall=True)
        tabela(self.registros)

    def registrar(self):
        """Valida cada inserção de registro e
        então os registra no banco de dados, caso
        sejam todos válidos
        """
        try:
            self.nome = valide(r'[a-zA-Z ]{1,30}', 'Nome: ')                                                            # Valida o nome inserido
        except ValueError:
            titulo('Nome inválido. Retornando ao menu...')
        else:
            try:
                self.sexo = valide(r'M|F', 'Sexo: ')                                                                    # Valida o sexo inserido
            except ValueError:
                titulo('Sexo inválido. Retornando ao menu...')
            else:
                try:
                    self.nascimento = valide_nascimento('Nascimento[DD/MM/AAAA]: ')                                     # Valida o nascimento inserido
                except ValueError:
                    titulo('Nascimento inválido. Retornando ao menu...')
                else:
                    try:
                        self.telefone = valide(r'(\(?\d{2}\)?)?(-|\s)?(9\s?)?\d{4}(-|\s)?\d{4}', 'Telefone: ')          # Valida o telefone inserido
                    except ValueError:
                        titulo('Telefone inválido. Retornando ao menu...')
                    else:
                        try:
                            self.email = valide(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[\.[a-zA-Z]{2,4}', 'Email: ')         # Valida o email inserido
                        except ValueError:
                            titulo('Email inválido. Retornando ao menu...')
                        else:
                            self.execute(f"insert into pessoas values (default, '{self.nome}', '{self.sexo}', '{self.nascimento}', '{self.telefone}', '{self.email}');")
                            print('Registro adicionado com sucesso.')
    
    def alterar(self):
        pass
