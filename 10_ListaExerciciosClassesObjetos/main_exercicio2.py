from models_exercicio2.conta_banco import conta_banco

guilherme = conta_banco('Guilherme', 1000, 500, [])
pedro = conta_banco('Pedro', 500, 300, [])
conta = []
resposta = ''

while resposta != 'n':
    resposta = str(input(' (1) para CRIAR CONTA \n (2) para SACAR \n (3) para DEPOSITAR \n (4) para TRANSFERIR \n (5) para EXCLUIR CONTA \n (n) para encerrar \n Digite: '))

    if resposta == '1':
        
        print('_'*50)
        print('CRIANDO SUA CONTA: \n')

        titular = str(input('Escreva seu nome: '))

        conta.append(conta_banco(titular, 1500, 800, []))
        
        for dado in conta:
            print(f'O titular {dado.titular} criou sua conta com um saldo inicial de R$ {dado.saldo} e limite de R$ {dado.limite} ')
    
    if resposta == '2':
        
        print('_'*50)
        print('SAQUE: \n')

        usuario = str(input('Escreva o nome do titular da conta: '))

        if usuario == 'Guilherme':

            valor = int(input('Escreva o valor que deseja sacar: '))
            
            guilherme.sacar(valor)
            guilherme.exibir_historico()

        elif usuario == 'Pedro':

            valor = int(input('Escreva o valor que deseja sacar: '))
            
            pedro.sacar(valor)
            pedro.exibir_historico()

        else: 

            valor = int(input('Escreva o valor que deseja sacar: '))
            
            conta.sacar(valor)
            conta.exibir_historico()
            