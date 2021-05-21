salario_atual = float(input('Digite o valor do seu salário: R$'))
if salario_atual > 1250.00:
    aumento = (salario_atual * 10 / 100)
    print('Você receberá um aumento de R$ {:.2f}'.format(aumento))
    print('Seu salário passará a ser {:.2f}'.format(salario_atual + aumento))
else:
    aumento = (salario_atual * 15 / 100)
    print('Você receberá um aumento de R$ {:.2f}'.format(aumento))
    print('Seu salário passará a ser {:.2f}'.format(salario_atual + aumento))
