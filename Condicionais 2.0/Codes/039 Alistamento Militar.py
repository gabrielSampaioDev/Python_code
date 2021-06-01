from datetime import date
ano_nascimento = int(input('Em que ano você nasceu? '))
ano_atual = date.today().year
prazo = ano_atual - ano_nascimento
if prazo > 18:
    print('Prazo excedido. Alistamento deveria ter sido feito há {} ano(s)'.format(prazo - 18))
elif prazo == 0:
    print('Você deverá se alistar esse ano ({})!!'.format(ano_atual))
elif prazo < 18:
    print('Idade para alistamento ainda não alcançada. Restam {} ano(s)'.format(18 - prazo))