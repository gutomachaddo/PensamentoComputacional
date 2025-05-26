class Produto:
    def __init__(self, nome: str, preco: float, moeda: str):
        self.__nome = nome
        self.__preco = preco
        self.__moeda = "BRL"
    
    def __str__(self):
        info = f'Nome do produto: {self.__nome}\n'
        info += f'Preço do produto: {self.__preco:.2f}\n'
        info += f'Tipo de moeda: {self.__moeda}\n'
        return info
    
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, preco):
        self.__preco = preco
    
    def get_moeda(self):
        return self.__moeda

    def set_moeda(self, moeda):
        self.__moeda = moeda    
