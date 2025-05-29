import re

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao, email))

#Testes
emails = ['usuario@exemplo.com', 'nome.sobrenome@empresa.com.br',
          'invalido@', 'sem_arroba.com', '@dominio.com', 'guilherme.+_-p@ienh.com.br']

for email in emails:
    print(f"{email}: {'Valido' if validar_email(email) else 'Inválido'}")



