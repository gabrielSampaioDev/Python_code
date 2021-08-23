# INTRO
print('-=-'*20)
print('|', ' '*20, 'Números Primos', ' '*20, '|')
print('-=-'*20)
# ESCREVENDO UM NÚMERO
n = int(input('Digite um número: '))
tot = 0
# CONDICIONAL
for c in range (1, n + 1 ):
    if n % c == 0:
        print('\033[33m', end= ' ')
        tot += 1
    else:
        print('\033[31m', end= ' ')
    print('{}'.format(c), end= ' ')
print('\n\033[mO número ({}), foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('Por isso ele é Primo!')
else:
    print('Por isso ele não é primo!')


'''if n == 2 or n == 3 or n == 5 or n == 7:
        print('É um número primo.')
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print('Não é um número primo.')
    
else:
    print('É um número primo.')'''