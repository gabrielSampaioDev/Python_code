KM = float(input('Qual a quantidade de KMs rodados? '))
dias = int(input('Quantos dias de aluguel foram contabilizados? '))
vt = KM * 0.15 + dias * 60
print('Total do valor a pagar: R$ {:.2f}'.format(vt))
