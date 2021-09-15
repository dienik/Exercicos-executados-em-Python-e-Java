dezoito = masculino = novinha = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        dezoito+=1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo? [F/M]: ')).strip().upper()[0]
    if sexo in 'Mm':
        masculino+=1
    if sexo in 'Ff' and idade< 20:
        novinha+=1
    print('=-='*30)
    continuar =' '
    while continuar not in 'SN':
     continuar = str (input('Deseja  continuar? ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print(f'{dezoito}tem mais de 18 an0s {novinha} mulheres tem menos de 20, {masculino} homens foram cadastrados.')