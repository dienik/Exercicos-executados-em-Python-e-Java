from datetime import date
nascimento=int(input('ano de nascimento'))
atual = date.today().year
idade = atual - nascimento
if idade<=9:
    print('O atleta tem {} anos, portanto é Mirim'.format(idade))
elif 14>=idade>9:
    print('O aleta tem {} anos, portanto é infantil.'.format(idade))
elif 19>=idade>14:
    print('O atleta tem {} anos portanto é JÚNIOR'.format(idade))
elif 25>=idade>19:
    print('O atleta tem {} anos, portanto é SENIOR'.format(idade))
elif idade>25:
    print('O atleta tem {}, portanto ele é MASTER'.format(idade))
    