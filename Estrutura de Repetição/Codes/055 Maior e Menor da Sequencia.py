# INTRO
print('-=-'*20)
print('|', ' '*14, 'Maior e Menor da Sequência', ' '*14, '|')
print('-=-'*20)
# ESCREVENDO NÚMEROS
print('Digite 5 números para verificar qual o maior e menor')
# VARIÁVEIS
numero = int(input('Digite o 1º número: '))   # numero = Primeiro número digitado pelo usuário <-- Número Base
maior = numero
menor = numero
# CONDICIONAL
for c in range(2,6):
    
    n = int(input('Digite o {}º número: '.format(c)))    # n = Número digitado pelo usuário
    if n < maior:
        maior == maior + 0
    else:
        maior = n
    if n < menor:
        menor = n
    else:
        menor == menor +0
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))