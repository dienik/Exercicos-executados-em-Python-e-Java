maior = 0
menor = 0
for c in range(1, 6):
    peso = int(input('Digite o {} ªpeso'.format(c)))
    if c== 1:
        maior = peso
        menor = peso
    else:
        if peso<menor:
            menor = peso
        elif peso > maior:
            maior = peso
print('O maior peso foi {}, e o menor {}'.format(maior ,  menor))
