from models_exercicio3.filme import filme

matrix = filme('Matrix', 'Ficção Científica', 136, 0.0 )

while True:
    nota = float(input('Escreva a sua nota para o filme Matrix: '))

    if nota >= 0 and nota <= 10:
        break
    else:
        print('Nota inválida! Escreva uma nota entre 0 e 10.')

matrix.avaliar(nota)
matrix.exibir_informacoes()