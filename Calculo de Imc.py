
peso=float(input('Digite seu peso'))
altura=float(input('digite sua altura'))
a1=(altura**2)
imc=peso/a1
if 18.5 > imc:
    print('Abaixo do peso')
elif 25>=imc>18.5:
    print ('Peso ideal')
elif 30>=imc>25:
    print('Sobrepeso')
elif 40>=imc>30:
    print('obesidade')
elif imc>40:
    print('obesidade mórbida')
