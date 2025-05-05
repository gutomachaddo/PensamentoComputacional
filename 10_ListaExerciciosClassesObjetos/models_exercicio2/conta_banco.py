class conta_banco:
    
    def __init__(self, titular, saldo, limite, historico):

        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico 

    def depositar(self):
        self.saldo += 100

