print('\033[31m-=-\033[m'*20)
print('\033[31m|\033[m', ' '*20,'\033[36mFINANCIAMENTO',' '*21, '\033[m\033[31m|\033[m', )
print('\033[31m-=-\033[m'*20)

valor_casa = float(input('Qual o valor da \033[33mcasa\033[m? R$'))# Valor total da casa 
Salario = float(input('Qual o valor do seu \033[33msalário\033[m? R$'))# Valor do salário mensal recebido
prazo = int(input('Em quantos anos você irá \033[33mfinalizar o pagamento\033[m? '))# Prazo de quitação do AP
prestacao_mensal = valor_casa / (prazo * 12)
if prestacao_mensal > Salario * 30 / 100:
    print('Emprestimo\033[31m negado\033[m por exceder 30% do valor do seu salário')
else:
    print('Emprestimo\033[32m liberado com sucesso\033[m') 
print('O valor da prestação ficará: R${:.2f}'.format(prestacao_mensal))
