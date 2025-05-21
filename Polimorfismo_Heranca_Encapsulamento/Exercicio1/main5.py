from models5.veiculo import Veiculo
from models5.Moto import Moto
from models5.VeiculoEletrico import VeiculoEletrico

if __name__ == "__main__":
    veiculos = [
        Veiculo("HB20 1", "ABC1234"),
        Moto("XJ6 1", "DEF5678", 600),
        VeiculoEletrico("BYD 1", "GHI9012", 50),
        Veiculo("HB20 2", "ABC1234"),  
        Moto("XJ6 2", "JKL3456", 800),
        VeiculoEletrico("BYD 2", "DEF5678", 60), 
        Veiculo("HB20 3", "MNO7890"),
        Veiculo("HB20 4", "PQR1234"), 
    ]

    placas_vistas = set()
    placas_duplicadas = set()
    veiculos_por_placa = {}

    for veiculo in veiculos:
        placa = veiculo.get_placa()
        if placa in placas_vistas:
            placas_duplicadas.add(placa)
        else:
            placas_vistas.add(placa)
        if placa not in veiculos_por_placa:
            veiculos_por_placa[placa] = []
        veiculos_por_placa[placa].append(veiculo)

    print("--- Placas Duplicadas Encontradas ---")
    if placas_duplicadas:
        for placa_duplicada in placas_duplicadas:
            print(f"Placa: {placa_duplicada}")
            for veiculo in veiculos_por_placa[placa_duplicada]:
                veiculo.exibir_informacoes()
                print("---")
    else:
        print("Nenhuma placa duplicada encontrada.")