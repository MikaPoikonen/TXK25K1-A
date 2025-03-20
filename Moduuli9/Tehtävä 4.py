#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
from random import randint
class Auto():
    def __init__(self,rekisterinumero: str,huippunopeus,nopeus = 0,matka = 0):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.matka = matka
        self.nopeus = nopeus

    def kiihdytä (self,luku: int):
        self.nopeus += luku
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
             self.nopeus = 0

    def liikkuminen(self,aika: float):
        self.matka += self.nopeus * aika

def main():
    autot =[Auto(f"ABC-{i}",randint(100,200)) for i in range (1,11) ]
    i = True
    while i:
        for auto in autot:
            auto.kiihdytä(randint(-10,15))
            auto.liikkuminen(1)

            if auto.matka > 10000:
                i =False

    def key(auto):
        return auto.matka

    for auto in autot:
        print(f"Auto: ", auto.rekisterinumero,  "Maksiminopeus: ", auto.huippunopeus, "km/h", "Nopeus:", auto.nopeus, "Matka: ", auto.matka, "km")
main()