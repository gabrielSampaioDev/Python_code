from time import sleep
nome = str(input('Digite o seu nome completo: '))
print('Analisando seu nome...')
sleep(3)
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome todo tem {} letras'.format(len(nome)-nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0], len(dividido[0])))
