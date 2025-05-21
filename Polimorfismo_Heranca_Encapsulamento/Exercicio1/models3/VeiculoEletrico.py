from models3.Veiculos import Veiculo

class VeiculoEletrico(Veiculo):
    def __init__(self, modelo, consumo_kwh_km, bateria_atual_percentual=100):
        super().__init__(modelo)
        self.consumo_kwh_km = consumo_kwh_km
        self.bateria_atual_percentual = bateria_atual_percentual

    def calcular_consumo(self, distancia):
        return distancia * self.consumo_kwh_km

    def recarregar(self, porcentagem):
        if porcentagem > 0:
            self.bateria_atual_percentual += porcentagem
            print(f"Veículo elétrico '{self.modelo}' recarregado em {porcentagem}%. Bateria atual: {self.bateria_atual_percentual}%")
        else:
            print("A porcentagem de recarga deve ser um valor positivo.")

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Consumo: {self.consumo_kwh_km} kWh/km")
        print(f"Bateria Atual: {self.bateria_atual_percentual}%")