from .veiculo import Veiculo

class Carro(Veiculo):
    def calcular_consumo(self):
        consumo_por_km = 12  
        return self.distancia / consumo_por_km