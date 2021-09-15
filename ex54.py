from datetime import date
atual = date.today().year
cont = 0
tot = 0
for c in range(1, 8):
    n1 = int(input('Digite o ano que voce nasceu:'))
    n1 = atual - n1
    if n1 >= 18:
        cont += 1
    else:
        tot += 1
print('O total de pessoas maiores de 18 anos é {} e os menores são  {}'.format(cont, tot))
