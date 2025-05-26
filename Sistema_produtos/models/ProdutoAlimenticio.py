from Sistema_produtos.models.produto import Produto

class ProdutoAlimenticio(Produto):
    def __init__(self, nome: str, preco: float, moeda: str, tipo_alimento: str):
        super.__init__(nome, preco, moeda)
        self.__tipo_alimento = tipo_alimento

    def get_tipo_alimento(self):
        return self.__tipo_alimento

    def set_tipo_alimento(self, tipo):
        self.__tipo_alimento = tipo
    
    def __str__(self):
        info = super().__str__()
        info += f'Tipo: {self.__tipo_alimento}'

