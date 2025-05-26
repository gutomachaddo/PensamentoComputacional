from CadastroPlaca.Cadastro_placa import Cadastro
from CadastroPlaca.erros import PlacaInvalida

veiculo1 = Cadastro('FOX', 'ABC1D23')
print(veiculo1)

try:
    veiculo1.set_placa('JK90D99')
    print(veiculo1)
except PlacaInvalida as e:
    print(f"Erro de validação de placa: {e}")

try:
    veiculo1.set_placa('CDE2P43')
    print(veiculo1)
except PlacaInvalida as e:
    print(f"Erro de validação de placa: {e}")
