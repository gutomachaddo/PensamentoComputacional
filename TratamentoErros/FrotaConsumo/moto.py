from .veiculo import Veiculo

class Moto(Veiculo):
    def calcular_consumo(self, distancia):
        consumo_por_km = 20  
        return distancia / consumo_por_km