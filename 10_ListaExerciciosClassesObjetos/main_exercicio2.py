from models_exercicio2.conta_banco import conta_banco

guilherme = conta_banco('Guilherme', 1000, 500, [])
pedro = conta_banco('Pedro', 500, 300, [])

guilherme.sacar(100)
guilherme.depositar(200)
guilherme.transferir(pedro,200)
guilherme.exibir_historico()
pedro.sacar(100)
pedro.depositar(200)
pedro.exibir_historico()