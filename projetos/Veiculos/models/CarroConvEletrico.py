from .CarrosCombustao import CarrosCombustao
from .CarroEletrico import CarroEletrico

class CarroConvEletrico(CarrosCombustao, CarroEletrico):
    ''' Classe que implementa métodos específicos de um carro convert 
    em elétrico
    '''
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, 
                 valor_fipe: float, combustivel: str, nPortas: int, nRodas, nAssentos: int, 
                 nCilindradas: int, nCambio: int, nivel_combustivel: int, nivel_bateria: int, tipo_bateria:
                 str, autonomia: int) -> None:
        CarrosCombustao.__init__(self, placa, modelo, marca, ano, valor_fipe, combustivel, nPortas, nRodas,
                         nAssentos, nCilindradas, nCambio, nivel_combustivel)
        CarroEletrico.__init__(self, placa, modelo, marca, ano, cor, valor_fipe, combustivel, nPortas,nRodas, nAssentos,
                               nCilindradas, nCambio, nivel_combustivel, nivel_bateria, tipo_bateria, autonomia)

    def __str__(self) -> str:
        infor = super().__str__()
        infor += f'\nNivel de bateria: {CarroEletrico.get_nivel_bateria()}\n'
        infor += f'Tipo de bateria: {CarroEletrico.get_tipo_bateria()}\n'
        infor += f'Autonomia: {CarroEletrico.get_autonomia()}\n'
        return infor

    def abastecer(self, percentual_adicionado)-> bool: # Serve para dizer o que é o retorno, mas não é necessário
        """Método abastecer desativado

        Args: 
            percentual_adicionado: float
        Returns: 
            False, pois não pode abastecer
        
        """
        print('Carro convertido para elétrico! Não é mais possível abastecer!')
        return False
    
    
