class PIX:

    def __init__(self, titular: str, saldo: float, limite: float, historico: list, chavePIX: list):

        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__historico = historico 
        self.__chavePIX = chavePIX

    def getChavePIX(self):
        return self.__chavePIX
    

resposta = ''

print('BANCO:')
print('-'*15)

while resposta != 's':
    resposta = str(input('DIGITE:\n(0) PARA CRIAR CHAVE-PIX: \n(1) PARA REALIZAR UM PIX: '))

    if resposta == '0':
        titular = input('Insira o nome do titular para a conta: ')