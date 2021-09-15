#Calculo de litros de tinta por metros quadrados
l1=float(input("digite a largura da parede: "))
a1=float(input('qual a altura da parede? '))
ar=l1*a1
lt=ar/2
print('a area em metros quadrados é: {}, e precisa de {}litros de tinta'.format(ar, lt))