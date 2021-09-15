termo=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))
cont=0
mais = 10
total = 10
while mais!= 0:
    total= total + mais
    while cont <=total:
            print('{}->'.format(termo), end='')
            termo +=razao
            cont+=1
    print('pausa')
    mais=int(input('Quantos termos deseja mostrar a mais? '))
print('Progressão aritmética finalizada com {} termos'.format(total))