from random import randint
from time import sleep

print('-=-'*20)
print('|', ' '*16, 'JOGO DA ADIVINHAÇÃO V2', ' '*16, '|')
print('-=-'*20)
#VARIÁVEIS
escolha_usuario = 11
tentativas = 1
# CONDICIONAL PC
computador = randint(0, 10)
#print(computador)
print('=='*32)
print('Vou pensar em um número entre 0 e 10... Você consegue adivinhar? ')

# COMDICIONAL DO JOGO --------- WHILE
while escolha_usuario != computador:
# CONDICIONAL USUÁRIO
    print('=='*32)
    escolha_usuario = int(input('Escolha um número entre 0 e 10: '))
# CONDICIONAL DO JOGO --------- IF

    if escolha_usuario == computador:
        print('\033[1;92mParabéns! Você acertou!\033[m')
    else:
        if escolha_usuario < computador:
            print('\033[1;31mMais... Você errou\033[m, tente novamente.')
            tentativas += 1
        elif escolha_usuario > computador:
            print('\033[1;31mMenos... Você errou\033[m, tente novamente.')
            tentativas += 1
if tentativas == 1:
    print('Você tentou apenas {} vez e acertou!'.format(tentativas))
else:
    print('Você tentou {} vezes para acertar.'.format(tentativas))
print('=='*32)
