from models1.Carro import carro
from models1.Moto import moto
from models1.Caminhao import caminhao

Fox = carro('ACE9D48', 'Fox', 'Volkswagen', 
                  2013, 'Branco', 30000, 0)

fh = caminhao('BJE8P43', 'FH_540', 'Volvo', 2025, 
                 'Cinza', 302.500, 0)

xj6 = moto('LKM3OP08', 'XJ6', 'YAMAHA', 2009,
           'Preto', 32.264, 0)

print(Fox)
distancia = int(input('Informe a distancia que o carro irá percorrer: '))
litros = Fox.calcular_consumo(distancia)
print(f'O Fox irá consumir em {distancia} km de viagem {litros}')