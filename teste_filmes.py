# Funções

def divisao():
  print('_'*50)

def mensagem_inicial():
  print(' VOCÊ PODE ESCREVER O NOME E A NOTA \n DE ATÉ 1000 FILMES! ')
  print('-'*50)

def mensagem_filmes_notas():
  print('OS FILMES E NOTAS INSERIDOS NO CATÁLOGO FORAM:')

def mensagem_media():
  print(f'A MEDIA DAS NOTAS DOS FILMES É: \n {round(media, 2)}')

# Algorimto Filmes

# Inicio

i = 0
x = 0
media = 0.0
cadastro = []
resposta = ''
soma_notas = 0.0

mensagem_inicial()

while resposta != 'n' and x < 1000:
    filme = str(input('Escreva o nome do filme: '))
    filmes_cadastrados = [item['FILME:'] for item in cadastro]

    while filme in filmes_cadastrados:
        print('Esse filme já foi cadastrado! Insira outro filme.')
        filme = str(input('Escreva o nome de um filme diferente: '))

    nota = float(input('Escreva a nota (de 0.0 até 10.0) para esse filme: '))

    if 0.0 <= nota <= 10.0:
        cadastro.append({'FILME:': filme, 'NOTA': round(nota, 2)})
        soma_notas += nota
        x += 1
    else:
        print('Nota inválida! Deve ser entre 0.0 e 10.0.')

    if x == 1000:
        print('\nLimite máximo de 1000 filmes atingido.')
        break
    else:
        resposta = str(input('Digite (s) para continuar ou (n) para encerrar: '))

if x > 0:
    media = soma_notas / x

divisao()
mensagem_filmes_notas()
for i in range(x):
    print(cadastro[i])

divisao()
mensagem_media()

divisao()
if x >= 3:
    cadastro_ordenado = sorted(cadastro, key=lambda filme: filme['NOTA'])

    print("\n=== 3 PIORES FILMES AVALIADOS ===")
    for filme in cadastro_ordenado[:3]:
        print(f"{filme['FILME:']} - Nota: {filme['NOTA']}")

    print("\n=== 3 MELHORES FILMES AVALIADOS ===")
    for filme in cadastro_ordenado[-3:][::-1]:
        print(f"{filme['FILME:']} - Nota: {filme['NOTA']}")
else:
    print("\nNecessita ser inseridos 3 filmes ou mais para mostrar os piores e melhores!")

# Fim