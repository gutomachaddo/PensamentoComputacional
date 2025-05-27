from models_sistema.ConversorMoeda import ConversorMoeda
from models_sistema.erros import MoedaInvalida
from models_sistema.ProdutoAlimenticio import ProdutoAlimenticio
from models_sistema.ProdutoEletronico import ProdutoEletronico

try:
    nome = input('\033[1;32mDigite o nome do produto: \033[m')
    preco = float(input('\033[1;32mDigite o preço atual do produto: \033[m'))
    classe = input('\033[1;32mDigite a classe (ELETRÔNICO/ ALIMENTO): \033[m').strip().lower()

    if classe == "alimento":
        tipo = input('\033[1;32mDigite o tipo (REGULADOR/ CONSTRUTOR/ ENERGÉTICO): \033[m')
        produto = ProdutoAlimenticio(nome, preco, tipo)
    
    elif classe == 'eletronico':
        tipo = input('\033[1;32mDigite o tipo (COMPUTADOR/ CELULAR/ TABLET): \033[m')
        produto = ProdutoEletronico(nome, preco, tipo)
    
    else:
        print('Tipo de produto inválido.')
    
    print('Produto criado com sucesso!')
    print(produto)

    conversor = ConversorMoeda()

    try:
        if conversor.converte_preco_para_usd(produto):
            print("\nConversão para USD realizada com sucesso.")
        else:
            print("\nProduto já está em USD.")
    except MoedaInvalida as erro:
        print(f"Erro na conversão: {erro}")

    print("\nInformações atualizadas do produto:")
    print(produto)

except ValueError:
    print("Erro: preço inválido. Digite um número válido.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

    