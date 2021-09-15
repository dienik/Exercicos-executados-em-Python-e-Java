cont=0
print('~~' * 39)
print('Tabuada')
while True:
    print('=-='*20)
    n= int(input('Digite um numero para ver sua tabuada: '))
    if n < 0:
        break
    else:
        for cont in range(0,11):
            tabuada= n*cont
            print(f'{n} x {cont} = {tabuada}')
            cont+=1
print('Programa tabuada encerrado!')
