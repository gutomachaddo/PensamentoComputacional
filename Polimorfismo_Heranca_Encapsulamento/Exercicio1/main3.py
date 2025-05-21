from models3.carro import Carro
from models3.moto import Moto
from models3.VeiculoEletrico import VeiculoEletrico

if __name__ == "__main__":
    hb20 = Carro("HB20", 10)
    xj6 = Moto("XJ6", 25)
    eletrico = VeiculoEletrico("BYD Dolphin", 0.15, 60)

    veiculos = [hb20, xj6, eletrico]
    distancia_teste = 100  

    print("--- Cálculo de Consumo para Diferentes Veículos ---")
    for veiculo in veiculos:
        print(f"\nVeículo: {veiculo.modelo}")
        consumo = veiculo.calcular_consumo(distancia_teste)
        if isinstance(veiculo, VeiculoEletrico):
            print(f"Consumo para {distancia_teste} km: {consumo:.2f} kWh")
            try:
                porcentagem_recarga = int(input(f"Digite a porcentagem para recarregar o '{veiculo.modelo}': "))
                veiculo.recarregar(porcentagem_recarga)
            except ValueError:
                print("Entrada inválida para a porcentagem de recarga.")
        else:
            if consumo != float('inf'):
                print(f"Consumo para {distancia_teste} km: {consumo:.2f} litros")
            else:
                print(f"Consumo para {distancia_teste} km: Infinito (consumo zero)")

    print("\n--- Exibindo Informações dos Veículos ---")
    for veiculo in veiculos:
        veiculo.exibir_informacoes()
        print("---")