km=float(input('digite quantos km vc dirigiu: '))
dia=int(input('informe por quantos dias alugou: '))
td= dia*60
k2=0.15*km
dk=td+k2
print('o valor a pagar é: {:.2f}'.format(dk))