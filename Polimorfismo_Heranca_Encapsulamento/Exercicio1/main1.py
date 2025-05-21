from models1.Carro import carro
from models1.Moto import moto
from models1.Caminhao import caminhao

Fox = carro('ACE9D48', 'Fox', 'Volkswagen', 
                  2013, 'Branco', 30000, 12, 0)

fh = caminhao('BJE8P43', 'FH_540', 'Volvo', 2025, 
                 'Cinza', 302.500, 5, 0)

xj6 = moto('LKM3OP08', 'XJ6', 'YAMAHA', 2009,
           'Preto', 32.264, 20, 0)

print(Fox)
distancia = int(input('Informe a distancia que o carro irá percorrer: '))
Fox.calcular_consumo(12)
print(Fox)

print(xj6)
distancia = int(input('Informe a distancia que o carro irá percorrer: '))
xj6.calcular_consumo(12)
print(xj6)

print(fh)
distancia = int(input('Informe a distancia que o carro irá percorrer: '))
fh.calcular_consumo(12)
print(fh)

