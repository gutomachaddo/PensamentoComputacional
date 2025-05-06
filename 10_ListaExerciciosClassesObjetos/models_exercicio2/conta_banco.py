class conta_banco:
    
    def __init__(self, titular, saldo, limite, historico, n_vezes):

        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico 
        self.n_vezes = n_vezes

    def depositar(self, valor):
<<<<<<< HEAD
=======
        if valor > 0:
            self.saldo += valor
        else:
            print(f'O valor {valor} é inválido')

    def sacar(self, valor): # valor so acessado dentro do metodo sacar 
        if valor <= self.saldo:
            self.saldo -= valor
            print('saque realizado!')
        else: # Sem grana em conta e irá acessar o limite
            a = input(f"deseja utilizar o limite de R$ {self.limite}? (s) para continuar")
            if a == 's':
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= self.limite
                    print('saque realizado!')
                else:
                    print('Saldo e limite insuficientes!')
            else:
                print('Operação com limite cancelada!')


    def transferir(self):

    def exibir_historico(self):
   
    def exibir_saldo(self):
        
        


>>>>>>> 4b2a2dc2f6157151785656a00e32a28e2f722746

        self.saldo += valor
        self.n_vezes += 1
        self.historico.append([f'O titular {self.titular}, depositou {self.n_vezes} vez(es) o valor de R$ {valor}'])

    def sacar(self, valor1):

        if self.saldo >= valor1:
            self.saldo -= valor1
        
        else:
            if (self.saldo + self.limite) > valor1:
                resposta = str(input('Você deseja utilizar o limite? Digite(s) para usar: '))
                if resposta == 's':
                    self.saldo -= valor1
            
                else:
                    print('Sessão encerrada!')
    