n1 = int(input("Digite o primeiro valor: "))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != '5':
    print('''O que você deseja fazer?
    [1] SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NUMEROS
    [5]SAIR DO PROGRAMA''')
    opcao = (input('Digite o numero correspondente a sua opção: '))
    if opcao == '1':
        soma = n1 + n2
        print('A soma de {} + {} é igual a {}'.format(n1, n2, soma))
    elif opcao == '2':
        multiplicacao = n1 * n2
        print('A multiplicação de {} x {} é igual a {}: '.format(n1, n2, multiplicacao))
    elif opcao == '3':
        if n1 > n2:
            print('O maior é {}'.format(n1))
        else:
            print('O maior é: {}'.format(n2))
    elif opcao == '4':
        n1 = int(input('Digite primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == '5':
        print('Finalizando... VOLTE SEMPRE')
    else:
        print('opcao invalida: ')
    print('=-='*20)
print('Programa finalizado. Obrigado')
