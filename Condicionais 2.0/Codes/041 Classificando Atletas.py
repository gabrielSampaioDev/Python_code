from datetime import date
print('-=-'*20)
print('|', ' '*17, 'Classificando Atletas', ' '*16, '|')
print('-=-'*20)
data_nascimento = int(input('Digite a data de nascimento do Atleta: '))
data_atual = date.today().year
categoria = data_atual - data_nascimento
if categoria <= 9:
    print('Categoria: MIRIM')
elif categoria > 9 and categoria <= 14:
    print('Categoria: INFANTIL')
elif categoria > 14 and categoria <= 19: 
    print('Categoria: JUNIOR')
elif categoria == 20:
    print('Categoria: SÊNIOR')
elif categoria > 20: 
    print('Categoria: MASTER')
print(categoria)