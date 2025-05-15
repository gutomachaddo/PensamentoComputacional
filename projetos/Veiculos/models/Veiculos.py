class Veiculos:

    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float) -> None:
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__valor_fipe = valor_fipe

    def __str__(self) -> str:
        '''Retorna uma string com as informações do veículo'''
        infos = f"Placa: {self.__placa}\n"
        infos += f"Modelo: {self.__modelo}\n"
        infos += f"Marca: {self.__marca}\n"
        infos += f"Ano: {self.__ano}\n"
        infos += f"Cor: {self.__cor}\n"
        infos += f"Valor_Fipe: {self.__valor_fipe}\n"
        return infos
    
    # get e set são uma convenção
    # get = pegar
    # set = configurar/ alterar

    def getPlaca(self) -> str:
        ''' Retorna a placa do veículo'''
        return self.__placa
    
    def setValorFipe(self, valor) -> None:
        '''Método que altera o valor da Fipe do Veículo
        
        Argumento: valor (float): nova valor da Fipe
        saída: True se ok
        
        '''
        self.__valor_fipe = valor
        return True
