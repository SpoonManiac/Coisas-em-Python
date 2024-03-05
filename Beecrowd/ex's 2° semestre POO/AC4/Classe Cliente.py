import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

motor = sqlalchemy.create_engine('sqlite:///')
conexao = motor.connect()
Base = declarative_base(motor)
sessao = Session()
conexao.execute('''
                CREATE TABLE IF NOT EXISTS CLIENTE(
                CODIGO NTEGER   PRIMARY KEY,
                NOME    VARCHAR(50) NOT NULL,
                RENDA LOAT          NOT NULL)
                ''')

class Cliente(Base):
    __tablename__ = 'CLIENTE'
    codigo = Column('CODIGO', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(50))
    renda = Column('Renda', Float)

    def __init__(self, nome, renda):
        self.nome = nome
        self.renda = renda

def main():
    global sessao
    clientes = sessao.query(Cliente).all()
    with open('allta renda.txt', 'w') as arq:
        for cliente in clientes:
            if cliente.renda >= 5000.00:
                arq.write(f'Nome: {cliente.nome}\nRenda: R$ {cliente.renda}\n\n')
    conexao.close()
main()