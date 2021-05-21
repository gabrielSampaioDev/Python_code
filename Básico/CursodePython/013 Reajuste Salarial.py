salario = float(input('Informe o salário do seu funcionário: '))
aumento = (salario * 15) / 100
valortotal = salario + aumento
print('O valor atual que ficará o salário do seu funcionário será: R${:.2f}'.format(valortotal))
