print('-=-'*20)
print('|', ' '*19, 'Calculo de Média', ' '*19, '|')
print('-=-'*20)
nota_1 = float(input('Digite a primeira nota do aluno: '))
nota_2 = float(input('Digite a segunda nota do aluno: '))
media = (nota_1 + nota_2) / 2
if media < 5:
    print('Você foi \033[31mreprovado\033[m!!')

elif media >= 7:
    print('Você está \033[32maprovado\033[m!!')
    
elif media >= 5 or media < 7:
    print('Você está em \033[33mrecuperação\033[m!!')



print('Sua nota final foi {}.'.format(media))