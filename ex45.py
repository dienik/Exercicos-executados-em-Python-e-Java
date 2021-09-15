from random import randint
from time import sleep

print('Vamos jogar jokenpo?')
nome=str(input('Digite seu nome: '))
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''SUAS OPÇÕES SÃO:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('O computador escolheu:{}'.format(itens[computador]))
print('-=-'*20)
print('Voce escolheu {}'.format(itens[jogador]))
print('=-='*20)
if computador == 0: #pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('{} ganhou!'.format(nome))
    elif jogador == 2:
        print('Computador ganhou!')
if computador == 1: #papel
    if jogador == 0:
        print('Computador ganhou ganhou!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('{} ganhou!'.format(nome))

if computador == 2:#tesoura
    if jogador == 0:
        print('{} ganhou!'.format(nome))
    elif jogador == 1:
        print('Computador ganhou!')
    elif jogador == 2:
        print('EMPATE!')



