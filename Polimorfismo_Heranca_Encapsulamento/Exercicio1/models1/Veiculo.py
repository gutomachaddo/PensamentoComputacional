class Veiculo:

    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float) -> None:
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__valor_fipe= valor_fipe

    def __str__(self):
        info = f"Placa: {self.__placa}\n"
        info += f"Modelo: {self.__modelo}\n"
        info += f"Marca: {self.__marca}\n"
        info += f"Ano: {self.__ano}\n"
        info += f"Cor: {self.__cor}\n"
        info += f"Valor_Fipe: {self.__valor_fipe}\n"
        return info
        

         