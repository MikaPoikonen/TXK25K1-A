from random import *
print("arvaa luku")
luku = (randint (0,10))
while True:
    arvaus = int (input("anna luku: "))
    if arvaus ==luku:
        print("arvasit oikein")
        break
    elif arvaus < luku:
        print("Arvaamasi luku liian pieni")
    elif arvaus > luku:
        print("Arvaamasi luku liian iso")