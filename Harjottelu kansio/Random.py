import random
noppa1 = 0
noppa2 = 0
heitot = 0

while noppa1 !=6 or noppa2 !=6:
    noppa1 =random.randint(1,6)
    noppa2 =random.randint(1,6)
    heitot +=1
    print (noppa1,noppa2)
print ("heittojen määrä:" + str(heitot))