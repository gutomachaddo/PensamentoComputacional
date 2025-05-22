from FrotaConsumo.veiculos import Veiculo

class caminhao(Veiculo):
    def __init__(self, placa, nome_veiculo, consumo, numero_rodas):
        super().__init__(placa, nome_veiculo, consumo)
        self.__numero_rodas = numero_rodas

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'N° RODAS: {self.__numero_rodas}')
