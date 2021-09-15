from random import randint
from time import sleep
palpites = 1
n1 = int(input('digite um numero'))
pc = randint(0, 10)
print('-=-' * 20)
print('será que conseguiu acertar?')
print('analisando seu numero...')
print('-=-' * 20)
while n1 != pc:
    palpites += 1
    if n1 > 10:
        n1 = int(input('Valor inválido! Tente outra vez: '))
    else:
        if n1 > pc:
            n1 = int(input('Errou eu estou pensando em um numero menor, tente de novo: '))
            print('-=-' * 20)
            print('Analisando seu numero...')
            sleep(3)
        elif n1 < pc:
            n1 = int(input('Errou! Estou pensando em um numero maior, tente novamente!: '))
            print('=-=' * 20)
            print('Analisando seu numero ...')
            sleep(3)

print('Acertou em {} tentativas! Você é quase tão bom quanto eu em jogos de advinhação'.format(palpites))
