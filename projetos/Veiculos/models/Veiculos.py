class Veiculos:

    def __init__(self, modelo, marca, placa, ano, cor, velocidade, latitude, longitude):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade
        self.latitude = latitude
        self.longitude = longitude

    def acelerar(self):
        self.velocidade += 10
        nova_latitude = self.latitude + 1
        self.alterar_latitude(nova_latitude)
        print(f'O carro de placa {self.placa} foi acelerado até {self.velocidade} km/h')

    def frenar(self):

        if self.velocidade > 10:
            self.velocidade -= 10

    def mostrarInfos(self):

        print(f"O veículo {self.modelo}, de placa {self.placa} está a {self.velocidade} km/h")
        print(f"Lat: {self.latitude}, long: {self.longitude}")   

    def alterar_placa(self, placa):

        self.placa = placa
    
    def alterar_modelo(self, modelo):

        self.modelo = modelo

    def alterar_marca(self, marca):

        self.marca = marca
    
    def alterar_ano(self, ano):

        self.ano = ano

    def alterar_cor(self, cor):

        self.cor = cor

    def alterar_velocidade(self, velocidade):

        self.velocidade = velocidade

    def alterar_latitude(self, latitude):

        self.latitude = latitude

    def alterar_longitude(self, longitude):

        self.longitude = longitude