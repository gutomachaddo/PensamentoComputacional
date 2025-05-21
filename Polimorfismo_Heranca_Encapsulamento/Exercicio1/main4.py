from models4.veiculo1 import Veiculo

if __name__ == "__main__":
    try:
        meu_veiculo = Veiculo("Uno", "ABC1234")
        meu_veiculo.exibir_informacoes()

        print("\nTentando alterar a placa:")
        meu_veiculo.set_placa("DEF5678")
        meu_veiculo.exibir_informacoes()

        meu_veiculo.set_placa("GHIJ901")
        meu_veiculo.exibir_informacoes()

        meu_veiculo.set_placa("JKL90123")
        meu_veiculo.exibir_informacoes()

        meu_veiculo.set_placa("MNO-3456")
        meu_veiculo.exibir_informacoes()

        meu_veiculo.set_placa("PQR7890")
        meu_veiculo.exibir_informacoes()

    except ValueError as e:
        print(f"Erro ao criar veículo: {e}")