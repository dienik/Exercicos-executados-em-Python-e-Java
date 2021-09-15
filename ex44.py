print('{:=^40}'.format( 'Lojas KM' ))
valor=float(input('Digite o valor das compras: R$'))
print('Escolha uma opção de pagamento:')
print('''[1] A vista no dinheiro ou cheque:
[2] A vista no cartão
[3]Até 2x no cartão
[4]3X ou mais no cartão''')
opcao=int(input('Digite uma opção: '))
if opcao == 1:
    print('O VALOR DAS SUAS COMPRAS COM 10% DE DESCONTO FICOU: R${}'.format(valor-(valor * 10 / 100)))
elif opcao== 2:
    print('O VALOR DAS COMPRAS COM 5% DE DESCONTO FICOU: R${}'.format(valor-(valor * 5 / 100)))
elif opcao== 3:
    print('O VALOR DAS COMPRAS FICOU:R${}'.format(valor))
elif opcao== 4:
    t2= valor + (valor * 20 / 100)
    print('O VALOR DAS SUAS COMPRAS COM 20% DE JUROS FICOU: R${}'.format(t2))
    totpac=int(input('Em quantas parcelas deseja fazer?'))
    parcela=t2 /totpac
    print('A SUA COMPRA SERÁ DIVIDA EM {}X DE R${}'.format(totpac , parcela))
