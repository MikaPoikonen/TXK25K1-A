icao=set ()
lentokentta_lisaa={}

while True:
    toiminto=input("Valitse toiminto: lisää kenttä, haku tai lopeta")
    if toiminto=="lopeta":
        break
    elif toiminto=="lisää":
        koodi=input(print("Anna ICAO koodi:"))
        kentta=input(print("Anna Kentän nimi"))
        icao.add(icao)
    else:
        for i in icao:
            print(i)

