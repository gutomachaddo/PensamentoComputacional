from .veiculo import Veiculo

class Caminhao(Veiculo):
    def calcular_consumo(self):
        consumo_por_km = 5  
        return self.distancia / consumo_por_km