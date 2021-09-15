from typing import Tuple

time: tuple[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str] = ('Flamengo', 'Internacional', 'ATLÉTICO-MG', 'SÃO PAULO',
                                                                                                                   'Fluminense', 'Gremio', 'Palmeiras' ,
                                                                                                                   'Santos', 'Atletico PR', 'Bragantino',
                                                                                                                   'ceara', 'Corinthians', 'Atletico Goianiense', 'Bahia',
                                                                                                                   'Chapecoense', 'Fortaleza', 'Vasco', 'Goias', 'Coritiba', 'Bota Fogo')
print('Os primeiros 20 times da tabela são {}'.format(time))
print('==='*30)
print('Os 5 primeiros colocados foram {}'.format(time[0:5]))
print('==='*30)
print('Os 4 ultimos colocados foram{}'.format(time[-4:]))
print('==='*30)
print(sorted(time))
print('==='*30)
print('Chapecoense está localizada na {} ªposição '.format(time.index('Chapecoense')))
if 'Chapecoense' not in time:
    print('Chapecoense não está entre os 20 primeiros colocados.')
