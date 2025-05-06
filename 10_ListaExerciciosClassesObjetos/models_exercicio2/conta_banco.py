class conta_banco:
    
    def __init__(self, titular, saldo, limite, historico, n_vezes):

        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico 
        self.n_vezes = n_vezes

    def depositar(self, valor):

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
    