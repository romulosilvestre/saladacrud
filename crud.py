import mysql.connector
from mysql.connector import errorcode

class Crud:
    def __init__(self):
        self.config = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'senai@123',
            'database': 'saladamix'
        }

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(**self.config)
            self.cursor = self.conn.cursor()
            print("Conexão bem-sucedida!")
            return self.conn
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Existe algo errado no nome de usuário ou senha')  

            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('Banco de dados não encontrado')
            else:
                print(err)
            return None

    def inserir(self, nome_salada, ingredientes):
        if not self.conn.is_connected():
            print("Não há conexão com o banco de dados.")
            return False

        try:
            sql_insert = "INSERT INTO salada (nome, ingredientes) VALUES (%s, %s)"
            self.cursor.execute(sql_insert, (nome_salada, ingredientes))
            self.conn.commit()
            print("Salada inserida com sucesso!")
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao inserir salada: {err}")
            return False