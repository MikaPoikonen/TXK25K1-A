import math
def suhde(pizza,pizza2):
    if pizza>pizza2:
        print ("pizza 2 on halvempi")
    elif pizza==pizza2:print("Pizzat ovat yhtä halpoja")
    else: print("Pizza 1 on halvempi")
    return
halkaisija1=float(input("Anna halkaisija:" ))
hinta1= float (input("Anna ensimmäisen pizzan hinta: "))
ala1=(halkaisija1/2)**2*math.pi
suhde1=hinta1/(ala1/10000)
halkaisija2=float(input("Anna toisen pizzan halkaisija:" ))
hinta2= float (input("Anna toisen pizzan hinta: "))
ala2=float(halkaisija2/2)**2*math.pi
suhde2=hinta2/(ala2/10000)
pizza2=str(suhde2)
pizza=str(suhde1)
suhde(pizza,pizza2)