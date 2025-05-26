from Sistema_produtos.models.produto import Produto
from Sistema_produtos.models.erros import MoedaInvalida

class ConversorMoeda(Produto):
    def __init__(self):
        self.__eur_brl = 6.14
        self.__usd_brl = 5.05
        self.__eur_usd = 1.22
    
    def converte_preco_to_usd(self, produto: Produto) -> bool:
        atual_moeda = produto.get_moeda()

        if atual_moeda == 'USD':
            return False

        try:
            if atual_moeda == 'BRL':
                novo_preco = produto.get_preco() / self.__usd_brl
            elif atual_moeda == 'EUR':
                novo_preco = produto.get_preco() / self.__eur_usd
            else:
                raise MoedaInvalida(atual_moeda)
        
            produto.set_preco(novo_preco)
            produto.set_moeda("USD")
            return True

        except MoedaInvalida as e:
            print(e)
            return False
    
    def converte_preco_to_eur(self, produto: Produto) -> bool:
        atual_moeda = produto.get_moeda()

        if atual_moeda == 'EUR':
            return False

        try:
            if atual_moeda == 'BRL':
                novo_preco = produto.get_preco() / self.__eur_brl
            elif atual_moeda == 'USD':
                novo_preco = produto.get_preco() / self.__eur_usd
            else:
                raise MoedaInvalida(atual_moeda)
        
            produto.set_preco(novo_preco)
            produto.set_moeda("EUR")
            return True

        except MoedaInvalida as e:
            print(e)
            return False
    
    def converte_preco_to_brl(self, produto: Produto) -> bool:
        atual_moeda = produto.get_moeda()

        if atual_moeda == 'BRL':
            return False

        try:
            if atual_moeda == 'USD':
                novo_preco = produto.get_preco() / self.__usd_brl
            elif atual_moeda == 'USD':
                novo_preco = produto.get_preco() / self.__eur_brl
            else:
                raise MoedaInvalida(atual_moeda)
        
            produto.set_preco(novo_preco)
            produto.set_moeda("BRL")
            return True

        except MoedaInvalida as e:
            print(e)
            return False


