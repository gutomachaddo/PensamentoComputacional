class frota:

    def __init__(self):
        self.__frota = []
    
    def add_veiculo(self, veiculo: str):
        self.__frota.append(veiculo)
    
    def calcular_consumo(self, distancia):
        distancia / 12
    
    def consumo_total(self):
        consumo_total = 0
        for veiculo in self.__frota:
            consumo_total += veiculo.calcular_consumo(self.distancia)
        return consumo_total
        
        