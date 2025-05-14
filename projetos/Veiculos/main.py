from models.Veiculos import Veiculos
from models.CarrosCombustao import CarrosCombustao

voyage = Veiculos('BCE9D36', 'Voyage', 'Volkswagen', 
                  2018, 'Vermelho', 48000)

jetta_gli = CarrosCombustao('JDM9D36', 'Jetta GLI', 'Volkswagen',
                            2025, 'Vermelho', 250000, 'Gasolina', 8,
                            4, 5, 2000, 'AT 7')

print(jetta_gli)
print(voyage)