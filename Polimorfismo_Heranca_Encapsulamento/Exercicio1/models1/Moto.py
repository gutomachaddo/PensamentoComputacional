from .Veiculo import Veiculo

class moto(Veiculo):


    def __init__(self, placa, modelo, marca, ano, cor, valor_fipe, consumo: int):

        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)

        self.__consumo = consumo
    
    def calcular_consumo(self, distancia):
        self.__consumo = self.__consumo * distancia

    def __str__(self):
        infor = super().__str__()
        infor += f'Consumo: {self.__consumo} km/l'
        return infor