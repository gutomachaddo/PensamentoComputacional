from models5.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, placa, cilindradas):
        super().__init__(modelo, placa)
        self.cilindradas = cilindradas

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Cilindradas: {self.cilindradas}")