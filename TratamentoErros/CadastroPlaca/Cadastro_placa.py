class cadastro:

    def __init__(self, modelo, placa):
        self.__modelo = modelo
        self.__placa = self.__validacao_placa(placa)

    def __str__(self):
        infor = f'MODELO: {self.__modelo}\n'
        infor += f'PLACA: {self.__placa}'
        return infor

    def __validacao_placa(self, placa):
        if len(placa) == 7 and placa[:3].isalpha() and placa[:3].isupper() and placa[3:4].isdigit() and placa[4:5].isalpha() and placa[4:5].isupper() and placa[5:].isdigit():
            return placa
        return None

    def getPlaca(self):
         return self.__placa

    def setPlaca(self, nova_placa):
        placa_valida = self.__validacao_placa(nova_placa)
        if placa_valida:
            self.__placa = placa_valida


    
         
    
             
            
          
