from .erros import PlacaInvalida

class Cadastro:
    def __init__(self, modelo, placa):
        self.__modelo = modelo
        self.__placa = self.__validacao_placa(placa)

    def __str__(self):
        info = f'MODELO: {self.__modelo}\n'
        info += f'PLACA: {self.__placa}'
        return info

    def __validacao_placa(self, placa):
        if (
            len(placa) == 7 and
            placa[:3].isalpha() and placa[:3].isupper() and
            placa[3].isdigit() and
            placa[4].isalpha() and placa[4].isupper() and
            placa[5:].isdigit()
        ):
            return placa
        else:
            raise PlacaInvalida(f"Placa inválida: {placa}. O formato correto é LLLNLNN.")

    def get_placa(self):
        return self.__placa

    def set_placa(self, nova_placa):
        self.__placa = self.__validacao_placa(nova_placa)


    
         
    
             
            
          
