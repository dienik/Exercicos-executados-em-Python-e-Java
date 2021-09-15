somaidade = 0
mediaidade = 0
velho = 0
idadehomem = 0
novinha: int = 0
for c in range(1, 5):
    print('Dados {}º pessoa: '.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('SEXO  M/F : ')).strip().upper()
    somaidade += idade
    mediaidade = somaidade / 4
    if c == 1 and sexo in 'Mm':
        idadehomem = idade
        velho = nome
    if sexo in 'Mm' and idade > idadehomem:
        idadehomem = idade
        velho = nome
    if sexo in 'Ff' and idade<20:
        novinha+=1
print('O home mais velho tem {} anos e se chama {}'.format(idadehomem, velho))
print('A média de idade é : {}'.format(mediaidade))
print('A quantidade de moças de menos de 20 anos é: {}'.format(novinha))
