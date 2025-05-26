from models_sistema.produto import Produto

class ProdutoAlimenticio(Produto):
    def __init__(self, nome: str, preco: float, tipo: str):
        super().__init__(nome, preco, "BRL")
        self.__tipo = tipo

    def get_tipo_alimento(self):
        return self.__tipo

    def set_tipo_alimento(self, tipo):
        self.__tipo = tipo
    
    def __str__(self):
        info = super().__str__()
        info += f'Tipo do alimento: {self.__tipo}\n'
        return info

