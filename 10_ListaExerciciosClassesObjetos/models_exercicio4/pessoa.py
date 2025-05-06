class pessoa:

    def __init__(self, nome, idade, altura):
        
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def aniversario(self):
        
        self.idade += 1

    def crescer(self):

        self.altura += 0.01

    def exibir_info(self):

        print(
            f'{self.nome} tem {self.idade} anos, com altura de {self.altura} metros! '
        )
