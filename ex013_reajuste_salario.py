sal = float(input('Qual o valor atual de salario ? R$'))

percent = float(input('Qual o percentual de reajuste deste ano?'))

n_sal = sal+sal*percent

print('O salario com reajuste é R${:.2f}'.format(n_sal))

