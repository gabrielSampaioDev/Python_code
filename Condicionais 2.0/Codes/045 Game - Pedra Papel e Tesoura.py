import emoji
from random import randint
from time import sleep
# INTRO
print('-=-'*20)
print('|', ' '*24, 'JOKENPÔ', ' '*23, '|')
print('-=-'*20)
# ESCOLHA DO JOGADOR
print(emoji.emojize('[ 1 ] PEDRA :fist:', use_aliases= True))
print(emoji.emojize('[ 2 ] PAPEL :hand:', use_aliases= True))
print(emoji.emojize('[ 3 ] TESOURA :v:', use_aliases = True))
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
if computador == 1: # Pedra
    if jogador == 1:
        print(emoji.emojize('Computador :fist: X :fist: Jogador', use_aliases= True))
        print('Empate!')
    elif jogador == 2:
        print(emoji.emojize('Computador :fist: X :hand: Jogador', use_aliases= True))
        print('Jogador venceu!')
    elif jogador == 3:
        print(emoji.emojize('Computador :fist: X :v: Jogador', use_aliases= True))
        print('Computador venceu!')
elif computador == 2: # Papel
    if jogador == 1:
        print(emoji.emojize('Computador :hand: X :fist: Jogador', use_aliases= True))
        print('Computador venceu!')
    elif jogador == 2:
        print(emoji.emojize('Computador :hand: X :hand: Jogador', use_aliases= True))
        print('Empate!')
    elif jogador == 3:
        print(emoji.emojize('Computador :hand: X :v: Jogador', use_aliases= True))
        print('Jogador venceu!')
elif computador == 3: # Tesoura
    if jogador == 1:
        print(emoji.emojize('Computador :v: X :fist: Jogador', use_aliases= True))
        print('Jogador venceu!')
    elif jogador == 2:
        print(emoji.emojize('Computador :v: X :hand: Jogador', use_aliases= True))
        print('Computador venceu!')
    elif jogador == 3:
        print(emoji.emojize('Computador :v: X :v: Jogador', use_aliases= True))
        print('Empate!!')
