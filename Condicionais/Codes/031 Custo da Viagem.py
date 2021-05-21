distancia = float(input('Qual a distancia da viagem desejada? '))
if distancia <= 200:
    print('O valor da viagem ficará: R$ {:.2f}'.format(distancia * 0.50))
else:
    print('O valor da viagem ficará: R$ {:.2f}'.format(distancia * 0.45))
