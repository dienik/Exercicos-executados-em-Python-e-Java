#frase= curso em video pyton
#fatiamento
#frase[9]
#pulando caracteres
#frase[9:21:quantos caracteres pular]
#comprimento da frase
#len(frase)
#contar quantas vezes o caractere aparece
#frase.count('caractere')
#quantas vezes encontrou o caractere
#frase.find('caractere')
#in diz se tem ou nao a plavra na frase
#ex curso in frase
#replace
#frase.replace('pyton', 'android')
#maiusculas
#frase.upper()
#mantem as maiusculas e muda as minusculas por maiusculas
#lower
#frase.lower
#o mesmo só que em minusuclo
#frase.capotalize
#troca todas por minusculas e poe só a primeira em maiuscula
#frase.title
#mantem em minusculo e poe as primeiras letras de cada palavra em maiusculo
#frase,strip
#remove todos os espaços inuteis da string
#frase.rstrip ou frase.lstrip
#remove somente os ultimos espaços, remove somente os primeiros espaços
#dividir strings
#split é feito em seus espaços, vai ocorrer uma divisão dentro da string nos espaços
#join
#'-'.join junta a frase de novo para ser uma string só
frase= 'curso em video pyton'
print(frase)
print(frase[2:13])
print(frase[2::3])
print(len(frase))
print(frase.count('e'))
print(frase.find('e'))
frase=frase.replace ('curso',' aula')
print(frase)
frase= frase.upper()
print(frase)
frase=frase.lower()
print(frase)
frase=frase.capitalize()
print(frase)
frase=frase.title()
print(frase)
dividido=frase.split()
print(dividido)
print(dividido[1:3])

