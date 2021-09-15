n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
md = (n1 + n2) / 2
if md < 5:
    print('Reprovado')
elif 7 > md >= 5:
    print('Recuperação')
elif md>7:
    print('APROVADO')