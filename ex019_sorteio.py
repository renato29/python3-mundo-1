import random

n1= str(input('Digite o nome dos alunos: '))
n2= str(input('Digite o nome do segundo aluno '))
n3= str(input('Digite o nome do terceiro aluno '))
n4= str(input('Digite o nome do quarto aluno '))

lista=[n1,n2,n3,n4]

escolhe = random.choices(lista)
print('O escolhido foi {}'.format(escolhe))
