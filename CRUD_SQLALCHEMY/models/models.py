'''
    Projeto: SISTEMA DE CADASTRO DE USUÁRIOS
    Instituição/data - IENH (2025/01)
    Aluno/autor - Augusto

Arquivo que contém as classes que representam os modelos do banco de dados.

Classes:

- Usuario: classe que representa a tabela 'usuários' no banco de dados

'''


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base para nossos modelos
Base = declarative_base()

class Usuario(Base):
    '''
    Classe que representa a tabela 'usuarios' no banco de dados.
    Atributos:
    id (int): ID do usuário (primary key)
    nome (str): Nome do usuário (tamanho maximo de 50 caracteres)
    idade (int): Idade do usuário
    '''
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer)
def __repr__(self):
    return f"<Usuario(nome='{self.nome}', idade={self.idade})>"