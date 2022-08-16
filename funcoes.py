import mysql.connector
from main import *
import random 

class funcoes:
    def __init__(self):
        self.conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='q1w2e3',
        database='barb')
        self.meu_cursor = self.conexao.cursor()
        

    def cadastrar_participante(self, nome , cpf):
        lg = login (nome, cpf)
        comando_sql = f'insert into login ' \
                    f'(cpf, nome, telefone) value ' \
                        
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    