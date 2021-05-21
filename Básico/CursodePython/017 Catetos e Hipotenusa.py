'''from math import hypot
co = int(input('Digite o valor do cateto oposto: '))
ca= int(input('Digite o valor do cateto adjacente: '))
print('O valor do comprimento da hipotenusa é: {:.2f}'.format(math.hypot(co, ca)))'''

'''co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'. format(hi))'''

import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
