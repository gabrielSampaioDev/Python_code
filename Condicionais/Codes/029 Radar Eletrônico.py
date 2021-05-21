from time import perf_counter, sleep
velocidade_carro = float(input('Qual a velocidade que o carro estava? '))
print('PROCESSANDO...')
sleep(3)
if velocidade_carro > 80:
    multa = (velocidade_carro - 80) * 7
    print('Você foi \033[1;31m multado\033[m. O valor da multa é de: R$ \033[1;31m{:.2f}\033[m'.format(multa))
else:
    print('Sua velocidade é \033[32mpermitida\033[m na via!') 
print('Tenha um bom dia! \033[1;36mDirija com segurança.\033[m')
