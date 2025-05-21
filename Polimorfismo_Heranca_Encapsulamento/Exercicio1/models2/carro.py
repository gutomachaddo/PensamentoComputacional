from models2.veiculos import Veiculo

class carro(Veiculo):
    def __init__(self, placa, nome_veiculo, consumo, num_portas):
        super().__init__(placa, nome_veiculo, consumo)
        self.__num_portas = num_portas

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'N° PORTAS: {self.__num_portas}')