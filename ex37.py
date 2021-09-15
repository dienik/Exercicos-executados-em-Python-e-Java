n1 = int(input('Digite o numero: '))
n2 = int(input('Digite o outro valor: '))
if n1 > n2:
    print('O valor {} é maior'.format(n1))
elif n2 > n1:
    print('O valor {} é maior'.format(n2))
elif n1 == n2:
    print('Nenhum valor é maior, os dois são iguais')
