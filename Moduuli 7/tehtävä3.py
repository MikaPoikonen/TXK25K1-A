icao=set ()
lentokentta_lisaa={}

while True:
    toiminto=input("Valitse toiminto: lisää, haku tai lopeta: ")
    if toiminto=="lopeta":
        break
    elif toiminto=="lisää":
        koodi=input(print("Anna ICAO koodi: "))
        kentta=input(print("Anna Kentän nimi: "))
        icao.add(koodi)
        lentokentta_lisaa[koodi]=kentta
    elif toiminto=="haku":
        print(icao)
        icao_haku = input("Anna haluamasi ICAO: ")
        if icao_haku in lentokentta_lisaa:
            print(f"{lentokentta_lisaa[icao_haku]}")

