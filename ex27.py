n=str(input('digite seu nome: ')).strip()
nome = n.split()
print("prazer em te conhecer, seu primeiro nome é {} ".format(nome[0]))
print("e eu ultimo nome é {}".format(nome[len(nome)-1]))