from .Veiculos import Veiculos

class CarrosCombustao(Veiculos):
    """
    Classe que representa um carro de combustão, herda de Veículos
    """
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, 
                 valor_fipe: float, combustivel: str, nPortas: int, nRodas, nAssentos: int, 
                 nCilindradas: int, nCambio: int,) -> None:
        
        super().__init__(placa, modelo, marca,
                         ano, cor, valor_fipe)

        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nRodas = nRodas
        self.__nAssentos = nAssentos
        self.__nCilindradas = nCilindradas
        self.__nCambio = nCambio
    
    def __str__(self) -> str:
        infos = super().__str__()
        infos += f'Combustivel: {self.__combustivel}\n'
        infos += f'Numero de portas: {self.__nPortas}\n'
        infos += f'Numero de rodas: {self.__nRodas}'
        infos += f'Numero de assentos: {self.__nAssentos}\n'
        infos += f'Numero de cilindradas: {self.__nCilindradas}\n'
        infos += f'Câmbio: {self.__nCambio}\n'
        return infos
        
