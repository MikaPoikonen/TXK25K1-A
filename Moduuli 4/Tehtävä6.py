from random import randint
N=int (input("Anna arvottavien pisteiden määrä: "))
i = 0 #määritetään while funktiota N varten
n=0
while i<=N:
    x= randint(-1000, 1000)/1000 #neliön rajat -1 ja 1
    y= randint(-1000, 1000)/1000 #neliön rajat -1 ja 1
    if x**2+y**2<1:
        n += 1
    i += 1 #kun i ja N kohtaa funktio loppuu
pii= 4*n/N
print(pii)