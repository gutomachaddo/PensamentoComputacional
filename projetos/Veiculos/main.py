from models.Veiculos import Veiculos
from models.CarrosCombustao import CarrosCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletrico import CarroConvEletrico

voyage = Veiculos('BCE9D36', 'Voyage', 'Volkswagen', 
                  2018, 'Vermelho', 48000)

jetta_gli = CarrosCombustao('JDM9D36', 'Jetta GLI', 'Volkswagen',
                           2025, 'Vermelho', 250000, 'Gasolina', 8,
                           4, 5, 2000, 'AT 7', 24)

tesla_model_s = CarroEletrico(placa = 'JDN0A00', modelo='Tesla Model S', marca='Tesla',
                            ano=2021, cor='Branco', valor_fipe=950000, nAssentos=5, nPortas=4, 
                            nivel_bateria=65, tipo_bateria='Lítio', autonomia=491)

fusca_eletrico = CarroConvEletrico(placa='IAA0D36', modelo='Fusca 1600 Elétrico', marca='Volkswagen',
                            ano=1975, cor='Azul', valor_fipe= 70000,combustivel= 'Gasolina', nPortas=4, nRodas= 4,
                            nAssentos=5, nCilindradas=1600, nCambio='MT 4', nivel_combustivel=24, nivel_bateria=65, 
                            tipo_bateria='Litio', autonomia=150)


print(jetta_gli)

if jetta_gli.abastecer(100):
    print('Abastecido com sucesso!')
else:
    print('Erro ao abastecer')

print(jetta_gli)

print(fusca_eletrico)
if fusca_eletrico.abastecer(30):
    print('Abastecido com sucesso!')
else:
    print('Erro ao abastecer')

print(fusca_eletrico)
