from random import randint
maara = int(input("Anna arpakuutioiden määrä: "))
summa = 0

for i in range(maara):
    summa += randint(1, 6)

print("Arpakuutioiden summa on:", + summa)