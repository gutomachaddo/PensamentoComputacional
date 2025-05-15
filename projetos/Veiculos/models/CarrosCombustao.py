from .Veiculos import Veiculos

class CarrosCombustao(Veiculos):
    """
    Classe que representa um carro de combustão, herda de Veículos
    """
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, 
                 valor_fipe: float, combustivel: str, nPortas: int, nRodas, nAssentos: int, 
                 nCilindradas: int, nCambio: int, nivel_combustivel: int) -> None:
        
        Veiculos.__init__(placa, modelo, marca,
                         ano, cor, valor_fipe)

        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nRodas = nRodas
        self.__nAssentos = nAssentos
        self.__nCilindradas = nCilindradas
        self.__nCambio = nCambio
        self.__nivel_combustivel = nivel_combustivel
    
    def __str__(self) -> str:
        infos = super().__str__()
        infos += f'Combustivel: {self.__combustivel}\n'
        infos += f'Numero de portas: {self.__nPortas}\n'
        infos += f'Numero de rodas: {self.__nRodas}\n'
        infos += f'Numero de assentos: {self.__nAssentos}\n'
        infos += f'Numero de cilindradas: {self.__nCilindradas}\n'
        infos += f'Câmbio: {self.__nCambio}\n'
        infos += f'Nivel combustível: {self.__nivel_combustivel}'
        return infos
    
    def abastecer(self, percentual_adicionado: int) -> bool:
        ''' Méotodo para abastecer um carro a combustão
        Argumentos:
            percentual (int): percentual adicionado

        retorno:
            bool: True se foi possivel abastecer, e False caso não

        '''
        
        novo_percentual = self.__nivel_combustivel + percentual_adicionado
        if novo_percentual <= 100:
            self.__nivel_combustivel = novo_percentual
            return True
        return False

        
