from models_sistema.produto import Produto
from models_sistema.erros import MoedaInvalida

class ConversorMoeda:
    def __init__(self):
        self.__eur_brl = 6.14
        self.__usd_brl = 5.05
        self.__eur_usd = 1.22
    
    def converte_preco_para_usd(self, produto: Produto) -> bool:
        atual_moeda = produto.get_moeda()

        if atual_moeda == 'USD':
            return False

        if atual_moeda == 'BRL':
            novo_preco = produto.get_preco() / self.__usd_brl
        elif atual_moeda == 'EUR':
            novo_preco = produto.get_preco() * self.__eur_usd
        else:
            raise MoedaInvalida(atual_moeda)
        
        produto.set_preco(novo_preco)
        produto.set_moeda("USD")
        return True
    
    def converte_preco_para_eur(self, produto: Produto) -> bool:
        atual_moeda = produto.get_moeda()

        if atual_moeda == 'EUR':
            return False

        if atual_moeda == 'BRL':
            novo_preco = produto.get_preco() / self.__eur_brl
        elif atual_moeda == 'USD':
            novo_preco = produto.get_preco() / self.__eur_usd
        else:
            raise MoedaInvalida(atual_moeda)
        
        produto.set_preco(novo_preco)
        produto.set_moeda("EUR")
        return True
    
    def converte_preco_para_brl(self, produto: Produto) -> bool:
        atual_moeda = produto.get_moeda()

        if atual_moeda == 'BRL':
            return False

        if atual_moeda == 'USD':
            novo_preco = produto.get_preco() * self.__usd_brl
        elif atual_moeda == 'EUR':
            novo_preco = produto.get_preco() * self.__eur_brl
        else:
            raise MoedaInvalida(atual_moeda)
        
        produto.set_preco(novo_preco)
        produto.set_moeda("BRL")
        return True

