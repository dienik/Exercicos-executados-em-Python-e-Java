from random import randint
from time import sleep
vit=0
while True:
    jogador = int(input('Digite um numero: '))
    pc = randint(0 , 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar?')).strip().upper()[0]
        print(f'Você jogou {jogador} e o computador jogou {pc}', end='')
        print('Deu par' if total % 2 ==0 else print('Deu impar'))
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vit+=1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            vit +=1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar movamente .....')
print(f'Você perdeu após ganhar {vit} seguidas!')

