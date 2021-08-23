#INTRO 
print('-=-'*20)
print('|',' '*20,'MENU DE OPÇÕES', ' '*20, '|')
print('-=-'*20)
def menu():
    #VARIÁVEIS
    escolha_usuario = 4 # Irá loopar o programa
    soma = 0
    multiplicacao = 0
    maior = 0
    #CONDICIONAL USUÁRIO 
    while escolha_usuario == 4:
        primeiro_valor = int(input('Digite o primeiro valor: '))
        segundo_valor = int(input('Digite o segundo valor: '))
        print('=='*15)
        print('[ 1 ]    SOMAR')
        print('[ 2 ]    MULTIPLICAR')
        print('[ 3 ]    MAIOR')
        print('[ 4 ]    NOVOS NÚMEROS')
        print('[ 5 ]    SAIR DO PROGRAMA')
        print('=='*15)
        escolha_usuario = int(input('Digite o número da operação que você deseja realizar: '))
        print('=='*30)
        if escolha_usuario == 1:
            soma = primeiro_valor + segundo_valor
            print('O valor da soma de {} e {} é igual a: {}'.format(primeiro_valor, segundo_valor, soma))
        if escolha_usuario == 2:
            multiplicacao = primeiro_valor * segundo_valor
            print('O valor da multiplicação de {} e {} é igual a: {}'.format(primeiro_valor, segundo_valor, multiplicacao))
        if escolha_usuario == 3: 
            if primeiro_valor > segundo_valor:
                print('O primeiro valor digitado \033[1;34m{}\033[m é maior que o segundo valor digitado \033[1;34m{}\033[m'.format(primeiro_valor, segundo_valor))
            elif primeiro_valor < segundo_valor:
                print('O segundo valor digitado \033[1;34m{}\033[m é maior que o primeiro valor digitado \033[1;34m{}\033[m'.format(segundo_valor, primeiro_valor))
            else:
                print('Os valores digitados são iguais.')
        if escolha_usuario == 5:
            print('Você opitou por sair do programa.')
    print('FIM DO PROGRAMA.')
def continuidade():
    menu()
    continuar = str(input('Deseja continuar no programa [S/N]? ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Deseja continuar no programa [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        print('Fim do Programa')
    elif continuar == 'S':
        return menu()
continuidade()