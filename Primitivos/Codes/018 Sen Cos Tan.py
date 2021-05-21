'''import math
angulo = float(input('Qual o angulo? '))
print('O valor é: {:.2f}'.format((math.cos(angulo))))    <<<<<<<<<    ERRADO!!!!!
---------------------------------------------------------------------------------------------------------------------'''


'''import math
ang = float(input('Qual o angulo? '))
seno = math.sin(math.radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
cos = math.cos(math.radians(ang))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
tan = math.tan(math.radians(ang))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))'''

from math import radians, sin, cos, tan
ang = float(input('Digite o angulo: '))
seno = sin(radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
cosseno = cos(radians(ang))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang, cosseno))
tangente = tan(radians(ang))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tangente))

