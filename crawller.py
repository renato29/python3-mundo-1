import urllib.request
def getDollar():
    content = urllib.request.urlopen("https://www.melhorcambio.com/dolar-hoje").read()
    content = str(content)
    find = '<input type="hidden" value="'
    posicao = int(content.index(find) + len(find))
    Dolar = content[ posicao : posicao  + 4]
    return Dolar
def getEuro(): 
    content = urllib.request.urlopen("https://www.melhorcambio.com/euro-hoje").read()
    content = str(content)
    find = '<input type="hidden" value="'
    posicao = int(content.index(find) + len(find))
    Euro = content[ posicao : posicao  + 4]
    return Euro

def getTemper():
    content = urllib.request.urlopen("https://www.climatempo.com.br/previsao-do-tempo/cidade/321/riodejaneiro-rj").read()
    content = str(content)
    find = 'id="tempMax0">'
    posicao = int(content.index(find) + len(find))
    Maxima = content[ posicao : posicao  + 2]
        
        
    find = 'id="tempMin0">'
    posicao = int(content.index(find) + len(find))
    Minima = content[ posicao : posicao  + 2]
    return [Maxima,Minima]


print("Dolar: " + getDollar())
print("Euro: " +  getEuro())
temp = getTemper()
print("Temp. Maxima: " + temp[0])
print("Temp. Minima: " + temp[1])
