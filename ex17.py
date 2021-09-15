import math
'''co = float(input('digite o cateto oposto: '))
ca = float(input('digite cateto adjacente'))
hip = math.hypot(co, ca)
print ('a hipotenusa é{:.2f}'.format (hip))'''

co = float(input('digite o cateto oposto:'))
ca = float(input('digite cateto adjacente:'))
hip= (co**2 + ca**2) **1/2
print ('A hipotenusa é: {:.2f}'.format(hip))

