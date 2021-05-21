produto = float(input('Digite o valor do produto: '))
desconto = (produto * 52) / 100
valorTotal = produto - desconto
print('O produto com desconto ficará com o valor de: R${:.2f}'.format(valorTotal))
