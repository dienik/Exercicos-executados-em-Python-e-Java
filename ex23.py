n=int(input('digite um numero:'))
u= n //1 % 10
d= n //10 % 10
c= n //100 % 10
m= n //1000 % 10
print('a unidade é {} '.format(u))
print('a dezena é {} '.format(d))
print('a centena é: {} '.format(c))
print('o milhar é{} '.format(m))