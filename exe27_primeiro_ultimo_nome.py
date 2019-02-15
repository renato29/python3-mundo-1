n = str(input('difite seu nome completo')).strip()
#fatiamento de string
nome = n.split()
print(nome)
print('seu primeiro nome é {}'.format((nome[0])))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))
