sexo = str(input('Digite seu sexo M/F: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Por favor, digite um sexo válido: ')).strip().upper()[0]
print('Seu sexo é: {}'.format(sexo))
