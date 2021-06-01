print('-=-'*20)
print('|', ' '*15, 'ÍNDICE DE MASSA CORPORAL', ' '*15, '|')
print('-=-'*20)
altura = float(input('Digite sua altura(ex.: 1.70): '))
peso = float(input('Digite seu peso(ex.: 69.2): '))
imc = peso / (altura)**2
if imc <= 18.5:
    print('Abaixo do Peso.')
elif imc > 18.5 and imc < 25:
    print('Peso Ideal.')
elif imc >= 25 and imc < 30:
    print('Sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Obesidade.')
else:
    print('Obesidade Morbida.')
print('Seu IMC é: {:.2f}'.format(imc))