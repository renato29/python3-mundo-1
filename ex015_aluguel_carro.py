km =float(input('Quantos KM foi percorrido com o carro?'))
dias = int(input('Quantos dias foi alugado? '))
tarifadia = 60.0 * dias
kms = 0.15 * km
valor = kms + tarifadia

print('Total a pagar de R${:.2f}'.format(valor))
