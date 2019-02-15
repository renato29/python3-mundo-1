resposta="s"
n1=0
n2=0
#nao sabemos aqui quantas vezes o usuario ira repetir.#
while resposta=="s":
    N1 = float(input("digite o primeiro numero:"))
    N2 = float(input("digite o segundo numero:"))
    total = (N1+N2)/2
    print("resultado da medias: \n" + str (total))
    #repare aqui aqui ira aparecer a
    #frase e o programa ira continuar#
    resposta = input("Digite S para continuar: ")