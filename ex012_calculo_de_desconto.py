prod = float(input('Qual o valor do produto ??'))

desc = 0.05
desconto = prod*desc
valor_final = prod - desconto

print ('O valor final com desconto é de R${:.2f}'.format(valor_final))

