import psycopg2
from tkinter import messagebox


class ConexaoUsuario:

    """Metodo Construtor"""
    def __init__(self):
        """connetion recebe informacoes para conexao com postgre"""
        self.connection = psycopg2.connect(
            user="postgres",
            password="root",
            host="localhost",
            port="5432",
            database="teste"
        )

        """Instancia um objeto cursor"""
        self.cursor = self.connection.cursor()

        """Variavel que vai guardar o nome da tabela"""
        self.table_name = None

        """Variavel que vai guardar o SQL de insercao"""
        self.sql_insert = None
        self.sql_delete = None
        self.sql_query = None
        self.return_query = None

        """Variavel que vai guardar os valores a serem inseridos no banco
            tem que ser uma tupla ( )"""
        self.inserted_values = tuple()
        self.delete_value = None

        # Verificar o que estes comandos fazem na conexão
        #self.autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
        #self.connection.set_isolation_level(self.autocommit)

    def insert_user(self):
        try:
            """Instancia um objeto cursor"""
            self.cursor = self.connection.cursor()
            self.table_name = "usuarios"
            
            self.sql_insert = "INSERT INTO" + self.table_name + "(usuario, senha) VALUES(%s,%s)"
            
            self.cursor.execute(self.sql_insert, self.inserted_values)
            print("Registro inserido com sucesso!")
            

            """Realiza o commit na conexao(insere os dados no banco)"""
            self.connection.commit()
            messagebox.showinfo("Mensagem", "Usuário cadastrado com sucesso")

        except:
            print("Erro")
            self.connection = None

        finally:
            if self.connection != None:
                self.cursor.close()
                self.connection.close()
                print("Conexão com banco encerrada")
            
    
    def delete_user(self, delete_value):

        self.cursor = self.connection.cursor()
        self.delete_value = delete_value
        self.table_name = "usuarios"
        self.sql_query = "Delete from " + self.table_name + " where nome = %s "

        self.cursor.execute(self.sql_query, (self.delete_value,))
        self.connection.commit()
        # result = self.cursor.rowcount
        self.cursor.close()
        self.connection.close()

    def buscar_user(self, usuario):
        self.cursor = self.connection.cursor()
        self.table_name = "usuarios"
        self.sql_query = "Select usuario, senha from " + self.table_name + " where usuario = %s"
        self.cursor.execute(self.sql_query, (usuario,))
 
        self.return_query = self.cursor.fetchall()


        return self.return_query