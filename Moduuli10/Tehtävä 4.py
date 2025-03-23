from random import randint
class Auto:
    def __init__(self, rekisterinumero: str, huippunopeus: int):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, määrä: int):
        self.nopeus += määrä

        if self.nopeus > self.huippunopeus:
            self.nopeus == self.huippunopeus

        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunteja: float):
        self.kuljettu_matka += tunteja * self.nopeus

class Kilpailu():
    def __init__(self, nimi: str, kisan_pituus: int, autot: list):
        self.nimi = nimi
        self.kisan_pituus = kisan_pituus
        self.autot = autot

    def tuntikuluu(self):
        for auto in self.autot:
            auto.kiihdytä(randint(-10,15))
            auto.kulje(1)

    def tulostatilanne(self):
        def key(auto):
            return auto.kuljettu_matka
            self.autot.sort(Reverse = True, key = key)

        for auto in self.autot:
            print(f"Rekisteritunnus: {auto.rekisterinumero}  Huippunopeus: {auto.huippunopeus} Nopeus: {auto.nopeus}  kuljettu matka: {auto.kuljettu_matka}")
        print()

    def kilpailuohi(self):
        i = True
        for auto in self.autot:
            if auto.kuljettu_matka >= self.kisan_pituus:
                i = False
        return i

def main():
    kilpailu = Kilpailu("Suuri romuralli", 8000,[Auto(f"ABC-{i}", randint(100,200)) for i in range(1,11)])


    i = True
    tunti = 0
    while i:
        kilpailu.tuntikuluu()
        tunti +=1
        i = kilpailu.kilpailuohi()

        if tunti % 10 == 0:
            kilpailu.tulostatilanne()
    kilpailu.tulostatilanne()
main()