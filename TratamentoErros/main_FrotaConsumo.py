from FrotaConsumo.caminhao import caminhao
from FrotaConsumo.carro import carro
from FrotaConsumo.frota import frota
from FrotaConsumo.moto import moto
from FrotaConsumo.veiculos import Veiculo

Fox = carro('ACD9D47', 'Fox', 12, 4)
xj6 = moto('FCL9D39', 'XJ6', 20, 600)
sedan = carro('JKL5D52', 'HB20', 13, 4)
k_ninja = moto('LMN5D25', 'Kawasaki Ninja', 22, 650)
fh_540 = caminhao('AJK5D37', 'FH-540', 20, 10)

frota = frota()
frota.add_veiculo()
frota.add_veiculo(xj6)
frota.add_veiculo(sedan)
frota.add_veiculo(k_ninja)
frota.add_veiculo(fh_540)

frota.listar_veiculos()

distancia_viagem = float(input('Qual será a distância da viagem para a frota: '))

for veiculo in frota:
    print(f'{frota.self.nome_veiculo[veiculo]} consumiu {veiculo.calcular_consumo(distancia_viagem)} litros')