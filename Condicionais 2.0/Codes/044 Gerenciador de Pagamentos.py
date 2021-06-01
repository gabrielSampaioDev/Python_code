print('-=-'*20)
print('|', ' '*15, 'GERENCIADOR DE PAGAMENTOS', ' '*14, '|')
print('-=-'*20)

produto = float(input('Insira o valor do produtor: '))
print('Formas de Pagamento:')
print('1 - À vista (Dinheiro/Cheque)')# 10% de desconto
print('2 - À vista (Cartão)')# 5% de desconto
print('3 - Em até 2x no cartão')# Preço normal
print('4 - 3x ou mais no cartão')# 20% de juros
forma_pagamento = int(input('Selecione a forma de pagamento: '))
if forma_pagamento == 1:
    print('O valor a ser pago pelo produto é R${:.2f}'.format(produto - (produto* 10 / 100)))
    print('Forma de pagamento: À vista (Dinheiro/Cheque)')
elif forma_pagamento == 2:
    print('O valor a ser pago pelo produto é R${:.2f}'.format(produto - (produto * 5 / 100)))
    print('Forma de pagamento: À vista (Cartão)')
elif forma_pagamento == 3:
    print('Valor a ser pago por parcela será R${:.2f}'.format(produto / 2))
    print('Forma de pagamento: Parcelado 2x no cartão')
elif forma_pagamento == 4:
    parcelas = int(input('Digite a quantidade de parcelas(ex.: 3): '))
    print('O valor a ser pago por parcela será R${:.2f}'.format((produto + (produto * 20 / 100)) / parcelas))
    print('Forma  de pagamento: Parcelado {}x no cartão'.format(parcelas))