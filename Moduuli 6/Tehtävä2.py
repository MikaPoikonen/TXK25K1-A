def nopat():
    print(noppa)
    return
from random import randint
luku= int(input("anna nopan luku"))
while True:
    noppa = randint(1,luku)
    nopat()
    if noppa == luku:
        break