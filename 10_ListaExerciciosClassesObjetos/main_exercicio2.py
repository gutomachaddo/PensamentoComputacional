from models_exercicio2.conta_banco import conta_banco

guilherme = conta_banco('Guilherme', 1000, 500, [])
guilherme.depositar(50)
pedro = conta_banco('Pedro', 500, 300, [])

guilherme.transferir(pedro, 50)
guilherme.exibir_historico()
pedro.exibir_historico()