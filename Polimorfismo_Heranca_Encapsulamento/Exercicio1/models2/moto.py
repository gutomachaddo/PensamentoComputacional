from models2.veiculos import Veiculo

class moto(Veiculo):

    def __init__(self, placa, nome_veiculo, consumo, cilindradas):
        super().__init__(placa, nome_veiculo, consumo)
        self.__cilindradas = cilindradas

    def exibir_informacoes(self):
        super().exibir_informacoes()
        infor += f'N° CILINDRADAS: {self.__cilindradas}'
        