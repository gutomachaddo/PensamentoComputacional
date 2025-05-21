from models2.veiculos import Veiculo

class frota:
    def __init__(self):
        self.__veiculos = []
    
    def add_veiculo(self, veiculo):
        if isinstance(veiculo, Veiculo):
            self.__veiculos.append(veiculo)
        
        else:
            print('ERRO')
    
    def listar_veiculos(self):
        if not self.__veiculos:
            print('A frota não contém veículos!')
            return
        print('\n ----LISTA DE VEICULOS DA FROTA----')
        for veiculo in self.__veiculos:
            veiculo.exibir_informacoes()
            print('-'*10)
        
    def calcular_consumo_total(self, distancia):
        consumo_total = 0
        for veiculo in self.__veiculos:
            consumo = veiculo.calcular_consumo(distancia)
            consumo_total += consumo
        return consumo_total
    

        
    
    