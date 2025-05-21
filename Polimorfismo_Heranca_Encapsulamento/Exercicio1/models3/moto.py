from models3.Veiculos import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, consumo_km_litro):
        super().__init__(modelo)
        self.consumo_km_litro = consumo_km_litro

    def calcular_consumo(self, distancia):
        if self.consumo_km_litro > 0:
            return distancia / self.consumo_km_litro
        else:
            return float('inf')

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Consumo: {self.consumo_km_litro} km/litro")
        