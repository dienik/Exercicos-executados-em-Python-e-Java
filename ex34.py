sl=float(input('digite seu salário atual: '))
sr=(sl*15/100)+sl
sm=(sl*10/100)+sl
if sl<=1250:
    print('com o aumento seu salário ficará R${}'.format(sr))
else:
    print('com o aumento de salário, voce receberá: {}'.format(sm))
