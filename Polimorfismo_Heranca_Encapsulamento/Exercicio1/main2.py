from models2.veiculos import Veiculo
from models2.frota import frota
from models2.carro import carro
from models2.moto import moto

Fox = carro('ACD9D47', 'Fox', 12, 4)
xj6 = moto('FCL9D39', 'XJ6', 20, 600)
sedan = carro('JKL5D52', 'HB20', 13, 4)
k_ninja = moto('LMN5D25', 'Kawasaki Ninja', 22, 650)

frota = frota()
frota.add_veiculo(Fox)
frota.add_veiculo(xj6)
frota.add_veiculo(sedan)
frota.add_veiculo(k_ninja)

frota.listar_veiculos()

distancia_viagem = float(input('Digite quantos Km de viagem: '))

consumo_total = frota.calcular_consumo_total(distancia_viagem)
print(f'O consumo total da frota para {distancia_viagem} km: {round(consumo_total, 2)} litros')