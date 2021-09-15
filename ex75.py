num =(int(input('Digite um numero: ')),
      int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
        int(input('Digite um numero: ')))
print(f'Você digitou os valores {num} ')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero tres apareceu na {num.index(3)+1}ªposição')
else:
    print('O numero tres não aparece na lista')
print('Os valores pares digitados foram:  ', end= '' )
for n in num:
    if n % 2 ==0:
        print(n, end=', ')
