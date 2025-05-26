from .veiculo import Veiculo

class Moto(Veiculo):
    def calcular_consumo(self):
        consumo_por_km = 20  
        return self.distancia / consumo_por_km