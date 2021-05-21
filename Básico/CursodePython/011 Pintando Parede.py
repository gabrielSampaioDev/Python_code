largura = float(input('Digite (em metros) a largura da parede: '))
comprimento = float(input('Digite (em metros) o comprimento(altura) da parede: '))
area = largura * comprimento
litro = area / 2
print('A area tem {:.2f}M²\nSerá preciso {} litro(s) de tinta.'.format(area, litro))
