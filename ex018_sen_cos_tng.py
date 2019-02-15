import math

ang = float(input('digite o angulo que vc deseja: '))
seno = math.sin(math.radians(ang))
print('>> o angulo de {}º tem o seno de {:.2f}'.format(ang,seno))
coss = math.cos(math.radians(ang))
print('>> o angulo de {}º tem o cosseno de {:.2f}'.format(ang,coss))
tg = math.tan(math.radians(ang))
print('>> o angulo de {}º tem a tangente de {:.2f}'.format(ang,tg))

