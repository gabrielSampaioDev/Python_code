from time import sleep
print('-=-'*20)
print('|', ' '*18, 'Comparando Números', ' '*18, '|')
print('-=-'*20)
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
if primeiro_numero > segundo_numero:
    print('O primeiro valor ({}) é maior'.format(primeiro_numero))
    print('O segundo valor ({}) é menor'.format(segundo_numero))
elif primeiro_numero < segundo_numero:
    print('O segundo valor ({}) é maior'.format(segundo_numero))
    print('O primeiro valor ({}) é menor'.format(primeiro_numero))
else:
    print('Não existe valor maior. {} e {} são iguais!'.format(primeiro_numero, segundo_numero))