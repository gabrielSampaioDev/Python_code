'''sexo = ['M', 'F']
resposta = 's'
while resposta == sexo:
    resposta = str(input('Qual o seu sexo [M/F]? ')).upper()
    if resposta != 'M' or resposta != 'F':
        print('Dados inválidos.')
    else:
        print('Dado registrado com sucesso!!')
print('Acabou!')'''
sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0] 
# .Strip irá fatiar .upper irá deixar a 1ª letra maiúscula, [0] para puxar somente a primeira letra caso a pessoa escreva 'Masculino' ou 'Feminino'
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor informe seu sexo [M/F]: ')).strip().upper()[0]
if sexo == 'F':
    print('Sexo \033[1;33mFeminino\033[m. Dados registrados com sucesso.')
else:
    print('Sexo \033[1;33mMasculino\033[m. Dados registrado com sucesso')