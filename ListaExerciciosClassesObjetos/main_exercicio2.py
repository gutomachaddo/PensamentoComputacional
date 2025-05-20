from models_exercicio2.conta import conta_banco
from time import sleep

guilherme = conta_banco('Guilherme', 1000, 500, [], ['1', '2'])
pedro = conta_banco('Pedro', 500, 300, [], ['3'])
contas = [pedro, guilherme]
resposta = ''

print('_' * 15)
print('\033[1;34m SERVIÇOS DO BANCO:\033[m')
print('-'*15)
print('CARREGANDO SERVIÇOS...')
sleep(2)
print('\n \033[1;36mSEJA BEM VINDO! Como podemos lhe ajudar hoje?\033[m')

while resposta != '11':
    resposta = str(input('\033[1;33m\n DIGITE:\n (1)  CRIAR CONTA: \n (2)  EXIBIR SALDO: \n (3)  SACAR: \n (4)  DEPOSITAR: \n (5)  TRANFERIR: \n (6)  HISTÓRICO DE TRANSAÇÕES: \n (7)  EXCLUSÃO DE CONTA: \n (8)  PARA CRIAR CHAVE PIX: \n (9)  PARA EXIBIR CHAVE PIX: \n (10) PARA FAZER PIX: \n (11) PARA SAIR: \033[m '))
    print('-' * 15)

    if resposta == '1':
        nome = str(input('Escreva o nome do titular: '))
        saldo = float(input('O saldo inicial que será adicionado: '))
        limite = float(input('O limite para sua nova conta: '))
        nome_existente = any(conta.titular == nome for conta in contas)
        if nome_existente:
            print('\033[1;31mEste nome já está sendo utilizado!\033[m\nDigite um nome diferente para realizar o cadastro.')
        else:
            contas.append(conta_banco(nome, saldo, limite, [], []))
            print(f'\033[1;32mConta criada com sucesso para o titular\033[m \033[1;36;46m{nome}\033[m!')

    elif resposta == '2':
        titular = str(input('Insira o nome do titular da conta: '))
        encontrado = False
        for conta in contas:
            if conta.titular == titular:
                print(f'O {titular} possui atualmente:\nSALDO: R$ {conta.saldo}')
                encontrado = True
                break
        if not encontrado:
            print('Conta Inexistente!')

    elif resposta == '3':
        titular = str(input('Insira o nome do titular da conta: '))
        for conta in contas:
            if conta.titular == titular:
                valor_saque = float(input('Insira o valor para saque: '))
                conta.sacar(valor_saque)
                break 

    elif resposta == '4':
        titular = str(input('Insira o nome do titular da conta: '))
        for conta in contas:
            if conta.titular == titular:
                valor_deposito = float(input('Insira o valor para depósito: '))
                conta.depositar(valor_deposito)
                break 

    elif resposta == '5':
        titular_envio = str(input('Insira o nome do titular da conta que irá realizar a transferência: '))
        conta_destino_nome = str(input('Insira o nome do titular da conta que irá receber a transferência: '))
        conta_envio = None
        conta_destino = None
        for conta in contas:
            if conta.titular == titular_envio:
                conta_envio = conta
            if conta.titular == conta_destino_nome:
                conta_destino = conta

        if conta_envio and conta_destino:
            valor_transferencia = float(input('Insira o valor que irá transferir: R$ '))
            conta_envio.transferir(conta_destino, valor_transferencia)
        else:
            print('Alguma das contas não foi encontrado o titular!')

    elif resposta == '6':
        titular = str(input('Insira o nome do titular da conta: '))
        encontrado = False
        for conta in contas:
            if conta.titular == titular:
                conta.exibir_historico()
                encontrado = True
                break
        if not encontrado:
            print('Conta Inexistente!')

    elif resposta == '7':
        titular_exclusao = str(input('Insira o nome do titular da conta para exclusão: '))
        conta_excluir = None
        for conta in contas:
            if conta.titular == titular_exclusao:
                conta_excluir = conta
                break

        if conta_excluir:
            tipo_exclusao = str(input('DIGITE:\n(0) PARA TRASNFERIR O SALDO RESTANTE PARA OUTRA CONTA\n(1) PARA SACAR O VALOR RESTANTE: '))
            if tipo_exclusao == '0':
                destinatario = str(input('Insira o nome do titular que irá receber a transferência: '))
                conta_destino_transferencia = None
                for conta_envio in contas:
                    if conta_envio.titular == destinatario:
                        conta_destino_transferencia = conta_envio
                        break
                if conta_destino_transferencia:
                    valor = conta_excluir.saldo 
                    conta_excluir.transferir(conta_destino_transferencia, valor)
                    contas.remove(conta_excluir)
                    print(f'CONTA DE {titular_exclusao} EXCLUÍDA E SALDO TRANSFERIDO PARA {destinatario}!')
                else:
                    print('Conta de destino para transferência não encontrada.')

            elif tipo_exclusao == '1':
                valor_saque_exclusao = conta_excluir.saldo 
                conta_excluir.sacar(valor_saque_exclusao)
                contas.remove(conta_excluir)
                print(f'CONTA DE {titular_exclusao} EXCLUÍDA E SALDO SACADO!')

            else:
                print('Opção de exclusão inválida.')
        else:
            print('Conta para exclusão não encontrada!')
    
    elif resposta == '8':
        titular = str(input('Insira o nome do titular da conta: '))        
        encontrado = False
        for conta in contas:
            if conta.titular == titular:
                if len(conta.chave_pix) == 2:
                    print('Esta conta já possui 2 chaves PIX!')
                    encontrado = True
                else:
                    pix1 = str(input('DIGITE O N° DE TELEFONE OU E-MAIL PARA CRIAR A CHAVE: '))
                    conta.chave_pix.append(pix1)
                    if len(conta.chave_pix) > 1:
                        print('CHAVE PIX CRIADA COM SUCESSO!\nATINGIDO O LIMITE DE CHAVES.')
                        encontrado = True
                    else:
                        resposta2 = str(input('DESEJA ADICIONAR OUTRA CHAVE? DIGITE:\n(s) PARA SIM\n(n) PARA NÃO\n----->'))
                        if resposta2 == 's':
                            pix2 = str(input('Insira a outra chave (TELEFONE ou E-MAIL): '))
                            conta.chave_pix.append(pix2)
                            print('CHAVES CRIADAS COM SUCESSO!')
                            ecnontrado = True
                        else:
                            print('CHAVE PIX CRIADA!\nSERVIÇO ENCERRADO.')
                            encontrado = True
                            break
        if not encontrado:
            print('Conta Inexistente!')
    
    elif resposta == '9':
        titular = str(input('Insira o nome do titular da conta: '))
        encontrado = False
        for conta in contas:
            if conta.titular == titular:
                print(f'Suas chaves PIX são essas:\n{conta.chave_pix}')
                encontrado = True
        if not encontrado:
            print('Conta Inexistente')
    
    elif resposta == '10':
        titular_envio = str(input('Insira o nome do titular da conta que irá realizar o PIX: '))
        conta_destino_nome = str(input('Insira o nome do titular da conta que irá receber o PIX: '))
        conta_envio = None
        conta_destino = None
        for conta in contas:
            if conta.titular == titular_envio:
                conta_envio = conta
            if conta.titular == conta_destino_nome:
                conta_destino = conta
                if conta_envio and conta_destino:
                    pix = str(input('Insira a chave PIX da pessoa: '))
                    if pix in conta_destino.chave_pix:
                        valor = float(input('VALOR DO PIX: R$ '))
                        conta_envio.transferir(conta_destino, valor)
                        print('PIX FEITO!')
                    else:
                        print('CHAVE PIX NÃO ENCONTRADA!')
                else:
                    print('Alguma das contas não foi encontrada!')
           
    elif resposta == '11':
        print('FINALIZANDO...')
        sleep(2)
        print('\033[1;36mOS SERVIÇOS DO BANCO FORAM FINALIZADOS!\033[m')

    else:
        print('Procurando serviço...')
        sleep(2)
        print('Nenhuma das opções digitadas é válida.')



    


