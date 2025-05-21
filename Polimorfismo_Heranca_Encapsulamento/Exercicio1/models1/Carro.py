from .Veiculo import Veiculo

class carro(Veiculo):


    def __init__(self, placa, modelo, marca, ano, cor, valor_fipe, consumo: int, litros_gastos: int):

        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)

        self.__consumo = consumo
        self.__litros_gastos = litros_gastos
    
    def calcular_consumo(self, distancia):
        self.__litros_gastos = distancia / self.__consumo 
    
    def __str__(self):
        infor = super().__str__()
        infor += f'Consumo: {self.__consumo} km/l\n'
        infor += f'Litros gastos na viagem: {self.__litros_gastos} litro(s)'
        return infor

        


        
    
