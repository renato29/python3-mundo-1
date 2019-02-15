idade = int(input("digite a sua idade\n"))

if idade < 16:
      print("vc ainda n pode votar\n")
elif idade >= 16 and idade <18:
    print("Parabens, vc pode votar\n")
elif  idade >18 and idade <65:
  print("Parabens, vc deve votar\n")
elif idade >=18 and idade>=65:
    print("Sr(a). se quiser passear aproveite para votar\n")
    

