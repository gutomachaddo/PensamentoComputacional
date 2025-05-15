from .Veiculos import Veiculos

class CarroEletrico(Veiculos):
    ''' Classe que implementa métodos específicos de carros elétricos

    Argumentos: Classe pai Veiculo

    '''

    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float,
                 nAssentos: int, nPortas: int, nivel_bateria: int, tipo_bateria: str, autonomia: int):
        Veiculos.__init__(placa, modelo, marca, ano, cor, valor_fipe)

        self.__nAssentos = nAssentos
        self.__nPortas = nPortas
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia

    def __str__(self) -> str:
        info = super().__str__()
        info += f'Numero de assentos: {self.__nAssentos}\n'
        info += f'Numero de portas: {self.__nPortas}\n'
        info += f'Nivel da bateria: {self.__nivel_bateria}\n'
        info += f'Tipo de bateria: {self.__tipo_bateria}\n'
        info += f'Autonomia: {self.__autonomia}\n'
        return info
    
    def get_nivel_bateria(self):
        return self.__nivel_bateria
    
    def get_tipo_bateria(self):
        return self.__tipo_bateria
    
    def get_autonomia(self):
        return self.__autonomia