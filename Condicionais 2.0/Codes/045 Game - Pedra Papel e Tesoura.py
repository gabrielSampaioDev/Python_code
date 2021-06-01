from random import randint
from time import sleep
# INTRO
print('-=-'*20)
print('|', ' '*24, 'JOKENPÔ', ' '*23, '|')
print('-=-'*20)
# ESCOLHA DO JOGADOR
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
jogador = int(input('Digite a sua jogada: (ex: 2): '))
sleep(1)
print('\033[1;31mJO\033[m')
sleep(1)
print('\033[1;31mKEN\033[m')
sleep(1)
print('\033[1;31mPÔ\033[m')
sleep(1)
# ESCOLHA DO COMPUTADOR
computador = randint(1, 3)
    # Pedra -> 1
    # Papel -> 2
    # Tesoura -> 3
# CONDICIONAL
if computador == 1:
    if jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Escolhi Papel. Ganhei!!')
    elif jogador == 3:
        print('Escolhi Tesoura. Você venceu...')
elif computador == 2:
    if jogador == 1:
        print('Escolhi Pedra. Você venceu...')
    elif jogador == 2:
        print('Empate!')
    elif jogador == 3:
        print('Escolhi Tesoura. Ganhei!!')
elif computador == 3:
    if jogador == 1:
        print('Escolhi Pedra. Ganhei!!')
    elif jogador == 2:
        print('Escolhi Papel. Você venceu...')
    elif jogador == 3:
        print('Empate!!')
