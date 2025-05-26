from Sistema_produtos.models.erros import MoedaInvalida
from Sistema_produtos.models.ConversorMoeda import ConversorMoeda
from Sistema_produtos.models.ProdutoAlimenticio import ProdutoAlimenticio
from Sistema_produtos.models.ProdutoEletronico import ProdutoEletronico

try:
    nome = input('Digite o nome do produto: ')
    preco = input('Digite o preço atual do produto: ')
    classe = input('Digite a classe (ELETRÔNICO/ ALIMENTO): ').strip().lower()

    if classe == "alimenticio":
        tipo_alimento = input('Digite o tipo (REGULADOR/ CONSTRUTOR/ ENERGÉTICO): ')
        produto = ProdutoAlimenticio(nome, preco, tipo_alimento)
    
    elif classe == 'eletronico':
        tipo_eletronico = input('Digite o tipo (COMPUTADOR/ CELULAR/ TABLET): ')
        produto = ProdutoEletronico(nome, preco, tipo_eletronico)
    
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