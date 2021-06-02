from time import sleep
print('-=-'*20)
print('|', ' '*14, 'Conversor de Base Númerica', ' '*14, '|')
print('-=-'*20)
numero_escolhido = int(input('Digite um valor inteiro qualquer: '))
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
base_escolhida = int(input('Para qual base você quer converter? '))
print('ANALISANDO...')
sleep(2)
if base_escolhida == 1:
    print('{} convertido em binário ficará {}'.format(numero_escolhido, bin(numero_escolhido)[2:]))
elif base_escolhida == 2:
    print('{} convertido em octal ficará {}'.format(numero_escolhido, oct(numero_escolhido)[2:]))
elif base_escolhida == 3:
    print('{} convertido para hexadecimal ficará {}'.format(numero_escolhido, hex(numero_escolhido)[2:]))
else:
    print('\033[31mOPÇÃO INVÁLIDA\033[m')