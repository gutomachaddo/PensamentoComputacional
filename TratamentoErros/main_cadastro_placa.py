from CadastroPlaca.Cadastro_placa import cadastro
from CadastroPlaca.erros import PlacaInvalida
try:
    veiculo1 = cadastro('FOX', 'ABC1D23')
    print(veiculo1)
    veiculo1.setPlaca('JK90D99')
    print(veiculo1)
    veiculo1.setPlaca('CDE2P43')
    print(veiculo1)
    

except Exception as PlacaInvalida:
    print(PlacaInvalida)
