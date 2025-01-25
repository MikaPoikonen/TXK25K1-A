from random import randint
arvottu = []
nopat = int (input("Anna noppien määrä"))



for i in range(nopat):
    arvottu_luku = randint(1, 6)
    arvottu.append(arvottu_luku)
    print(i)
for luku in arvottu:
    print (luku)