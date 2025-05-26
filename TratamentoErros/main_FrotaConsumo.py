from FrotaConsumo.carro import Carro
from FrotaConsumo.moto import Moto
from FrotaConsumo.caminhao import Caminhao
from FrotaConsumo.erros import DistanciaInvalida, ListaVazia


frota = [
    Carro('Gol'),
    Moto('Biz'),
    Caminhao('Scania'),
    Carro('Onix'),
    Moto('CG160')
]

try:
    if not frota:
        raise ListaVazia("A lista de veículos está vazia.")

    distancia = float(input("Informe a distância da viagem (em km): "))
    if distancia <= 0:
        raise DistanciaInvalida("A distância deve ser maior que zero.")

    print("\nConsumo estimado para cada veículo:")
    for veiculo in frota:
        consumo = veiculo.calcular_consumo(distancia)
        print(f"- {veiculo.modelo} - Consumo: {consumo:.2f} litros")

except DistanciaInvalida as e:
    print(f"Erro de distância: {e}")

except ListaVazia as e:
    print(f"Erro na frota: {e}")

except ValueError:
    print("Entrada inválida. Digite um número válido para a distância.")