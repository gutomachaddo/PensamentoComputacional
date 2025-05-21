from models5.veiculo import Veiculo

class VeiculoEletrico(Veiculo):
    def __init__(self, modelo, placa, capacidade_bateria):
        super().__init__(modelo, placa)
        self.capacidade_bateria = capacidade_bateria

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Capacidade da Bateria: {self.capacidade_bateria} kWh")