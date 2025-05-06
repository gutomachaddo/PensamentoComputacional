class conta_banco:
    
    def __init__(self, titular, saldo, limite, historico):

        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico 

    def depositar(self, valor):
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
        
        



