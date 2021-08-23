# INTRO
print('-=-'*20)
print('|', ' '*18, 'Analisador Completo', ' '*17, '|')
print('-=-'*20)
# VARIÁVEIS
soma_idade = 0  # Irá somar as idades
mais_velho = 0 # A idade do Homem mais velho
qtd_mulheres = 0 # Quantidade de mulheres que terá menos que 20 anos
# Calculará a média 
# CONDIÇÃO
for c in range(0,4):
    print('-=-'*15)
    nome = str(input('Digite o nome: ')).title()
    idade = int(input('Digite a idade: ')) 
    sexo = str(input('Digite o sexo (ex.: M ou F): ')).upper()
    if mais_velho < idade and sexo == 'M':
        mais_velho = idade
        maior_homem = nome
    else:
        mais_velho == mais_velho + 0
    soma_idade += idade
    if idade < 20 and sexo == 'F':
        qtd_mulheres = qtd_mulheres + 1
    else:
        qtd_mulheres = qtd_mulheres + 0
media_idade = soma_idade / 4
print('A média de idade do grupo é {:.0f} anos.'.format(media_idade))
print('O homem mais velho é o {}, e ele tem {} anos.'.format(maior_homem, mais_velho))
print('Há {} mulher(es) com menos de 20 anos.'.format(qtd_mulheres))
