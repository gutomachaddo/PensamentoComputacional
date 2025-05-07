import time

class conta_banco:

    '''
    Classe que implementa métodos para manipular uma conta bancária.add()
    Atributos: titular (str), saldo (float), limite (float), e histórico (lista de dicionários)

    OBS: Operações no histórico: 0 - sacar, 1- depositar, 2 - transferir

    '''

    def __init__(self, titular, saldo, limite, historico):

        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico 

        '''
        Construtor da classe conta_banco
        '''
    
    def depositar(self, valor):
        '''
        Método que realiza o depósito na conta bancária
        Entrada: Valor (float)
        Return: True (se a operação foi realizada com sucesso.)
                False (se a operação não foi realizada.)
        '''

        if valor > 0:
            self.saldo += valor
            self.historico.append({'operacao': 0,
                                   'remetente': self.titular,
                                    'destinatario': None, 
                                    'valor': valor,
                                    'saldo': self.saldo,
                                    'data/tempo': int(time.time())})
            return True
        else:
            print(f'O valor {valor} é inválido')
            return False

    def sacar(self, valor): 
        '''
        Método que realiza o saque da conta bancária
        Entrada: Valor (float)
        Return: True (se a operação foi realizada com sucesso.)
                False (se a operação não foi realizada.)
        '''
                
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({'operacao': 1,
                                   'remetente': self.titular,
                                    'destinatario': None, 
                                    'valor': valor,
                                    'saldo': self.saldo,
                                    'data/tempo': int(time.time())})
            print('saque realizado!')
            return True
        else: 
            a = input(f"deseja utilizar o limite de R$ {self.limite}? (s) para continuar")
            if a == 's':
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= self.limite
                    print('saque realizado!')
                    return True
                else:
                    print('Saldo e limite insuficientes!')
            else:
                print('Operação com limite cancelada!')

    def exibir_historico(self):
        print('Histórico de transações:')
        print('_'*150)
        for item in self.historico:
            dt = time.localtime(item['data/tempo'])
            print('Op:', item['operacao'],
                  '\n . Remetente:', item['remetente'],
                  '\n . Destinatário:', item['destinatario'],
                  '\n . Saldo:', item['saldo'],
                  '\n . Valor:', item['valor'],
                  '\n . Data e Tempo:',
                  str(dt.tm_hour) + ':' + str(dt.tm_min) + ':' + str(dt.tm_sec) + ' / DIA:' + str(dt.tm_mday) + ' MÊS:' + str(dt.tm_mon) + ' ANO:' + str(dt.tm_year))

    def transferir(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            

        else:
            print('Você não possui saldo suficiente!')
        
               
        