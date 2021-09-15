vm=float(input('escreva a velocidade do carro'))
vn=(vm-80)*7
if vm<=80:
    print('velocidade aceitavel')
else:
    print('voce ser MULTADO, sua multa será de {}'.format(vn))
