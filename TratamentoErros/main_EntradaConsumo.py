from EntradaDadosConsumo.carro import Carro
from EntradaDadosConsumo.moto import Moto
from EntradaDadosConsumo.caminhao import Caminhao


while True:
    try:
        distancia = float(input("Informe a distância da viagem (em km): "))
        if distancia <= 0:
            raise ValueError("A distância deve ser maior que zero.")
        break
    except ValueError as e:
        print(f"Entrada inválida: {e}")

while True:
    tipo = input("Informe o tipo de veículo (Carro, Moto ou Caminhao): ").strip().lower()

    if tipo == "carro":
        veiculo = Carro(distancia)
        break
    elif tipo == "moto":
        veiculo = Moto(distancia)
        break
    elif tipo == "caminhao":
        veiculo = Caminhao(distancia)
        break
    else:
        print("Tipo de veículo inválido. Escolha entre Carro, Moto ou Caminhao.")

consumo = veiculo.calcular_consumo()
print(f"\nO consumo estimado para a viagem é de {consumo:.2f} litros de combustível.")
