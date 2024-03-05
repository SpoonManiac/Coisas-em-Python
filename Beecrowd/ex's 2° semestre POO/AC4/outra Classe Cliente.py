import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

motor = sqlalchemy.create_engine('sqlite:///trabalho.db')
conexao = motor.connect()
Base = declarative_base(motor)
sessao = Session()
conexao.execute('''
                CREATE TABLE IF NOT EXISTS CLIENTE (
                    CODIGO INTEGER     PRIMARY KEY,
                    NOME VARCHAR(50)   NOT NULL,
                    RENDA FLOAT        NOT NULL)
                ''')

class Cliente(Base):
    tablename = 'CLIENTE'
    codigo = Column ('CODIGO', Integer, primarykey=True, autoincrement=True)
    nome = Column ('NOME', String(50))
    renda = Column ('RENDA', Float)

    def init(self, nome, renda):
        self.nopme = nome
        self.renda = renda

def main():
    nome = input('\Nome?')
    while nome != '':
        renda = float(input('Renda? R$ '))
        sessao.add(Cliente(nome, renda))
        sessao.commit()
        nome = input('\Nome? ')
    conexao.close()

main()