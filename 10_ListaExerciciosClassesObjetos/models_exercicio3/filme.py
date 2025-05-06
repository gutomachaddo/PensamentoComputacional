class filme:

    def __init__(self, titulo, genero, duracao, avaliacao):

<<<<<<< HEAD
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao 
        self.avaliacao = avaliacao

    def avaliar(self, nota):
        if nota >= 0 and nota <= 10:
            self.avaliacao = nota

    def exibir_informacoes(self):
        print(
            f'O filme {self.titulo}, do genênero de {self.genero}, com duração de \n aproximadamente {self.duracao} minutos, recebeu a nota de {self.avaliacao}'
        )
    
=======
    self.titulo = titulo
    self.genero = genero
    self.duracao = duracao 
    self.avaliacao = avaliacao

    def avaliar(self):
        self
        
>>>>>>> 4b2a2dc2f6157151785656a00e32a28e2f722746

