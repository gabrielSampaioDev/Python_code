from datetime import date
print('Grupo de Maioridade.')
data_atual = date.today().year
maioridade = 0 
menoridade = 0
for c in range(0, 7): 
    data_nascimento = int(input('Digite o ano de nascimento: '))
    if data_atual - data_nascimento > 18:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1
print('{} pessoa(s) já atigiram a maioridade.'.format(maioridade))
print('{} pessoa(s) ainda \033[1;31mnão\033[m atingiram a maioridade.'.format(menoridade))