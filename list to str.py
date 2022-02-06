import random

numerofstreaks=0
coinflip=[]
streak=0

for experimentnumber in range(10000):
    for i in range(100):
        coinflip.append(random.randint(0,1))

for i in range(len(coinflip)):
    if coinflip[i]==coinflip[i-1]:
        streak+=1
    else:
        streak=0
    if streak==6:
        numerofstreaks+=1
print('chance of streak:%s%%'%(numerofstreaks/100))
