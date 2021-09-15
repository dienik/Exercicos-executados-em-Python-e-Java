resposta = 's'
soma = cont = media = 0
maior = 0
menor = 0
while resposta in 'Ss':
    valor = int(input('Digite um valor: '))
    soma +=valor
    cont +=1
    resposta=str(input('Deseja ler mais algum valor? ')).strip().upper()[0]
    if cont ==1:
        maior = valor
        menor = valor
    else:
        if valor<menor:
            menor = valor
        else:
            maior = valor

media = soma / cont
print(' Foram lidos {} valores e  a média é {}, o menor valor é {} e o maior {} '.format(cont, media, menor, maior))

