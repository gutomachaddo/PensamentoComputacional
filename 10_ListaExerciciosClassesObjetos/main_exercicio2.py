from models_exercicio2.conta_banco import conta_banco

conta = conta_banco('Alfredo Neto', 1000, 500, [])
conta_destino = conta_banco('Joaquim Neto', 500, 300, [])


conta.depositar(150)
conta.exibir_historico()
conta.sacar(100)
conta.exibir_historico()
conta.transferir(50)
conta_destino.exibir_historico()