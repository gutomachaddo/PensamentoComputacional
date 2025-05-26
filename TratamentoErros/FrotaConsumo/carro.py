from .veiculo import Veiculo

class Carro(Veiculo):
    def calcular_consumo(self, distancia):
        consumo_por_km = 12 
        return distancia / consumo_por_km