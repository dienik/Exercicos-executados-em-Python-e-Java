cont = 0
n1 = int(input('Digite um numero para  ver se ele é primo: '))
for c in range(1, n1 + 1):
    if n1 % c == 0:
        cont = cont + 1
        print('\033[35m', end='')
    else:
        print('\033[m', end='')
    print('{}'.format(c), end='')
print('\n\033[m0 numero {} foi divisivel {} vezes'.format(n1, cont))
if cont ==2:
    print('é primo')
else:
    print('Não é primo')
