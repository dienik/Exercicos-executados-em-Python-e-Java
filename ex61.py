termo=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))
cont=0
while cont <=10:
        print('{}->'.format(termo), end='')
        termo +=razao
        cont+=1
print('fim')