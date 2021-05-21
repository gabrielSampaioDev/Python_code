from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "Pensar"
print('-=-'*19)
print('Vou pensar em um número entre o 0 e 5... Tente adivinhar!')
print('-=-'*19)
jogador = int(input('Que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Você errou! Eu pensei no número {} e não o número {}'.format(computador, jogador))
