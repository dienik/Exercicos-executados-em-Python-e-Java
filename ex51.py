print('PROGRESSÃO ARITMETICA')
print('-=-'*20)
t1=int(input('Primeiro termo:'))
r1=int(input('Razão:'))
dc=t1+(10-1)*r1
for c in range (t1,dc,r1):
    print('{}'.format(c), end='->')
print('ACABOU')
