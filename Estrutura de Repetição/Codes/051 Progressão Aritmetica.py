n1 = int(input('Digite um número: '))
pa = int(input('Digite a progressão: '))
decimo = n1 + (10- 1) * pa
for c in range(n1, decimo + pa, pa):
    print(c, end= ' → ')
print('Acabou')