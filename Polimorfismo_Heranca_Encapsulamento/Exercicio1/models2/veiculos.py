class Veiculo:

    def __init__(self, placa, nome_veiculo, consumo, ):
        self.__placa = placa
        self.__nome_veiculo = nome_veiculo
        self.__consumo = consumo

    def exibir_informacoes(self):
        print(f'PLACA: {self.__placa}')
        print(f'VEICULO: {self.__nome_veiculo}')
        print(f'CONSUMO: {self.__consumo}')
    
    def calcular_consumo(self, distancia):
        return distancia / self.__consumo
 


    
    