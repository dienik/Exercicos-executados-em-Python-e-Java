soma = 0
cont = 0
for c in range(1, 7):
    n1 = int(input('Digite o {} valor'.format(c)))
    if n1 % 2 == 0:
        soma +=n1
        cont+=1
print('Voce informou {} valores e a soma dos pares é: {}'.format(cont, soma))

