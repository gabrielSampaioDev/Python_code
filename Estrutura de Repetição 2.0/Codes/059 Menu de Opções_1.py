#INTRO 
print('-=-'*20)
print('|',' '*20,'MENU DE OPÇÕES', ' '*20, '|')
print('-=-'*20)

opção = 0
while opção != 5:
    primeiro_valor = int(input('Digite o primeiro valor: '))
    segundo_valor = int(input('Digite o segundo valor: '))
    print('=='*15)
    print('''    [ 1 ]    SOMAR
    [ 2 ]    MULTIPLICAR
    [ 3 ]    MAIOR
    [ 4 ]    NOVOS NÚMEROS
    [ 5 ]    SAIR DO PROGRAMA''')
    print('=='*15)
    opção = int(input('>>>> Qual é sua opção? '))
    if opção == 1:
        soma = primeiro_valor + segundo_valor
        print('O valor de {} + {} é igual a: {}'.format(primeiro_valor, segundo_valor, soma))
    elif opção == 2:
        multiplicacao = primeiro_valor * segundo_valor
        print('O valor de {} X {} é igual a: {}'.format(primeiro_valor, segundo_valor, multiplicacao))
    elif opção == 3:
        if primeiro_valor > segundo_valor:
            print('O primeiro valor digitado \033[1;34m{}\033[m é maior que o segundo valor digitado \033[1;34m{}\033[m'.format(primeiro_valor, segundo_valor))
        elif primeiro_valor < segundo_valor:
            print('O segundo valor digitado \033[1;34m{}\033[m é maior que o primeiro valor digitado \033[1;34m{}\033[m'.format(segundo_valor, primeiro_valor))
        else:
           print('Os valores digitados são iguais.')
    elif opção == 4:
        print('Informe os números novamente: ')
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*15)

print('FIM DO PROGRAMA! Volte sempre!')