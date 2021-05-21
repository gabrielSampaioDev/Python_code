num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}...'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
"""unidade = digitos[0]
dezena = digitos[1]
centena = digitos[2]
milhar = digitos[3]
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))"""
