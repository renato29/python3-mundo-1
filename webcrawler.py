import urllib.request

content = urllib.request.urlopen("https://www.melhorcambio.com/dolar-hoje").read()
content = str(content)
find = '<input type="hidden" value="'
posicao = int(content.index(find) + len(find))
dolar = content[ posicao : posicao  + 4]

content = urllib.request.urlopen("https://portaldobitcoin.com/cotacao-bitcoin/").read()
content = str(content)
find = '">R$'
posicao = int(content.index(find) + len(find))
bitcoin = content[ posicao : posicao  + 6]


content = urllib.request.urlopen("https://dolarhoje.com/ouro-hoje/").read()
content = str(content)
find = '<input type="text" id= "nacional" value="'
posicao = int(content.index(find) + len(find))
ouro = content[ posicao : posicao  + 6]

content = urllib.request.urlopen("https://br.investing.com/commodities/brent-oil").read()
content = str(content)
find = 'dir="ltr">'
posicao = int(content.index(find) + len(find))
brent = content[ posicao : posicao  + 5]


print("Dolar: " + dolar)
print("Bitcoin: " + bitcoin)
print("Ouro: " + ouro)
print("Petróleo Brent " + brent)
