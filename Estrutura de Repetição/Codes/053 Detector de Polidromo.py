frase = str(input('Digite uma frase: '))
frase_sem_espaço = frase.replace(' ', '').lower()
#print(frase_sem_espaço)
frase_invertida = frase_sem_espaço[::-1]
if frase_invertida == frase_sem_espaço:
    print('A frase \033[1;32m"{}"\033[m é um palídromo'.format(frase))
else:
    print('A frase \033[33m"{}"\033[m \033[1;31mnão\033[m é um palídromo'.format(frase))