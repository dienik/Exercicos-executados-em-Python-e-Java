from random import randint
from time import sleep
n1=int(input('digite um numero'))
pc=randint(0, 5)
print('\33[47;06;1m-=-'*20)
print('será que conseguiu acertar?')
print('analisando seu numero...')
sleep(3)
print('-=-'*20)
if n1==pc :
    print('acertou, pensamos igual')
else:
    print('PERDEU, o numero era {}'.format(pc))