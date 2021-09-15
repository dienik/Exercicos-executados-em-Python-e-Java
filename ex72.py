numeros = ('zero','um', 'dois', 'tres', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze','dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    n=int(input('Digite um numero entre zero e vinte: '))
    if 0 <= n <=20:
        break

print('Seu numero é {}'.format(numeros[n]))
