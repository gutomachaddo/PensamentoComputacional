from Sistema_produtos.models.produto import Produto

class ProdutoEletronico(Produto):
    def __init__(self, nome: str, preco: float, moeda: str, tipo_eletronico: str):
        super.__init__(nome, preco, moeda)
        self.__tipo_eletronico = tipo_eletronico

    def get_tipo_alimento(self):
        return self.__tipo_eletronico

    def set_tipo_alimento(self, tipo):
        self.__tipo_eletronico = tipo
    
    def __str__(self):
        info = super().__str__()
        info += f'Tipo: {self.__tipo_eletronico}'