from .veiculo import Veiculo

class Caminhao(Veiculo):
    def calcular_consumo(self, distancia):
        consumo_por_km = 5  
        return distancia / consumo_por_km
