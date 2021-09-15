menor = mais = soma = cont = barato =0
while True:
    nome = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto:R$ '))
    cont+=1
    soma += valor
    if valor > 1000:
        mais = mais + 1
    if cont ==1 or valor < menor:
        barato = valor
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print(f'''A soma é {soma:.2f}, 
o item mais barato foi {barato}
e foram comprados {mais} itens de mais de R$1.000.00''')
