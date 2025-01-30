lista = set()

while True:
   nimi=input("Anna nimi: ")
   if nimi=="":
       for i in lista:
           print(i)
       break
   if nimi not in lista:
       lista.add(nimi)
       print("uusi nimi")
   else:print("Annettu nimi oli jo listassa!")

