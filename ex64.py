n1 =0
cont=0
soma=0
while n1!= 999:
    cont+=1
    soma+=n1
    n1=int(input('Digite o {}ªvalor:  '.format(cont)))
print('Foram digitados {} numeros e a soma deles é {}'.format(cont, soma))
