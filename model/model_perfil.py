import psycopg2



class ModelPerfil:

    """Metodo Construtor"""
    def __init__(self):
        """connetion recebe informações para conexao com postgre"""
        self.connection = psycopg2.connect(
            user="postgres",
            password="root",
            host="localhost",
            port="5432",
            database="esquadriaDB"
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
        self.valor_procurado = ()

        """Variavel que vai guardar os valores a serem inseridos no banco
            tem que ser uma tupla ( )"""
        self.inserted_values = ()
        self.delete_value = None

        # Verificar o que estes comandos fazem na conexão
        # self.autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
        # self.connection.set_isolation_level(self.autocommit)
                
    def insert_perfil(self, insert):
        try:
            """Instancia um objeto cursor"""
            self.cursor = self.connection.cursor()
            self.table_name = "perfis"
            self.sql_insert = "INSERT INTO " + self.table_name + "(codigo, descricao, kgmetro, linha, comprimento) VALUES(%s,%s,%s,%s,%s)"
            self.cursor.execute(self.sql_insert, insert)
            
            """Realiza o commit na conexao(insere os dados no banco)"""
            self.connection.commit()
            print("Concluido", "Cadastro realizado com Sucesso!")

        except:
            print("Erro")
            self.connection = None

        finally:
            self.cursor.close()
            self.connection.close()

    def delete_perfil(self, delete_value):

        self.cursor = self.connection.cursor()
        self.delete_value = delete_value
        self.table_name = "perfis"
        self.sql_query = "Delete from " + self.table_name + " where codigo = %s "

        self.cursor.execute(self.sql_query, (self.delete_value,))
        self.connection.commit()
        # result = self.cursor.rowcount
        self.cursor.close()
        self.connection.close()

    def buscar_perfil(self):
        self.cursor = self.connection.cursor()
        self.table_name = "perfis"
        self.sql_query = "Select codigo from " + self.table_name
        self.cursor.execute(self.sql_query)
        
        self.return_query = self.cursor.fetchall()

        return self.return_query


    def pesquisar_perfil_produto(self):
        self.cursor = self.connection.cursor()
        self.table_name = "perfis"
        self.sql_query = "Select codigo, descricao, kgmetro, linha from " + self.table_name + " where descricao ilike " + self.valor_procurado
        self.cursor.execute(self.sql_query)
        
        self.return_query = self.cursor.fetchall()

        return self.return_query