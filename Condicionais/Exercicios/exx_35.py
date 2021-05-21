r1 = float(input('Digite o comprimento da PRIMEIRA reta: '))
r2 = float(input('Digite o comprimento da SEGUNDA reta: '))
r3 = float(input('Digite o comprimento da TERCEIRA reta: '))

if (r2 - r3) < r1 < r2 + r3 and (r1 - r3) < r2 < r1 + r3 and (r1 - r2) < r3 < r1 + r2:
    print('\033[1;32mÉ possível\033[m formar um triângulo!')
else:
    print('\033[1;31mNão\033[m é possível formar um triângulo!')