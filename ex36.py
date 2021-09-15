salario=float(input('Digite seu salário:R$ '))
casa=float(input('Digite o valor da casa: R$'))
anos=int(input('Em quantos anos quer pagar?'))
valor=float(salario *30 /100)
meses=int(anos*12)
parcela=int(casa/meses)
if  parcela > valor:
    print('Não aprovado')
elif parcela < valor:
    print('Aprovado!')
    print('Para comprar a casa de {}, O valor das parcelas será: {:.2f} em {:.2f}meses'.format(casa, parcela, meses))

