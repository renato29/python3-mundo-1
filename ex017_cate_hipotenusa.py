import math
cat_op = float(input('Digite um número do cateto oposto \n'))
cat_adj = float(input('Digite um número do cateto adjacente\n '))
"float(input('Digite o numero da hipotenusa'))"

hipo= math.hypot(cat_op,cat_adj)

print('hipotenusa vale {} '.format(hipo))

