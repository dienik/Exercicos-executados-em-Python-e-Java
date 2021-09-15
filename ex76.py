print(f'{"Listagem de preços":^30}')
print('==='*30)
lista=('ARROZ', 25.90,
       'FEIJÃO', 9.00,
       'MASSA', 3.79)
print("==="*30)
for pos in range(0, len(lista)):
    if pos % 2 ==0: #se o item da lista está em posição par
        print(f'{lista[pos]:.<30}', end= '')#alinhado a esquerda
    else:
        print(f'R${lista[pos]:.>7.2f}')#alinhado a direita