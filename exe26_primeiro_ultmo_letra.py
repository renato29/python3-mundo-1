frase = str(input('digite uma frase mano!')).upper()
#quantas vezes aparece a letra A#
print(' a letra A aparece {} vezes na frase mano.'.format(frase.count('A')))
#qual posição esta aparecendo cada letra
print (' A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
#qual a posição da ulima letra a
print('a ultima letra aparece na posição {}'.format(frase.rfind('A')+1))


