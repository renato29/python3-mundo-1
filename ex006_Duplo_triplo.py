n=int(input('Digite um número inteiro para o calculo de dobro, triplo e raiz quadrada:\n'))
d = n*2
t = n*3
r = n**(1/2)
print('o dobro de {}, vale {} '.format(n,d))
print('o triplo de {} vale {} '.format(n,t))
print('a raiz de {} vale {:.2f}'.format(n,r))
