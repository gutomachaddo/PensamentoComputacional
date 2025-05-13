class carro:
    def __init__(self, modelo: str, marca: str, velocidade: float) -> bool:
        self.__modelo = modelo
        self.__marca = marca
        self.__velocidade = velocidade

        return True

    def getModelo(self) -> str:
        return self.__modelo
    
carro.getModelo('fiat')


