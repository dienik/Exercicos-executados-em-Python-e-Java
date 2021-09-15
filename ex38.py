from datetime import date
atual=date.today().year
nasc=int(input('Digite seu ano de nascimento'))
idade=atual - nasc
tempo=idade
if idade ==18:
    print('Você tem que se alistar imediatamente!')
elif idade<18:
    saldo=18 - idade
    ano= atual + saldo
    print('Voce ainda não tem 18 anos, ainda faltam {} para o alistamento'.format(saldo))
    print('Voce se alistará em {}'.format(ano))

elif idade>18:
    saldo=idade-18
    ano=atual-saldo
    print('Você já era para ter se alistado há {} anos'.format(saldo))
    print('Você deveria ter se alistado em {}'.format(ano))
    