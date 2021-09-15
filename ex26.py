frase=str(input('digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira vez que a letra A aparece é{}'.format(frase.find('A')+1))
print('a ultima letra A foi encontrada em {}'.format(frase.rfind('A')+1))