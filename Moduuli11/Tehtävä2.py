class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def Aja(self,tuntia:int):
        self.tuntia = tuntia
        self.kuljettu_matka = self.tuntia * self.tämänhetkinen_nopeus

    def tulosta(self):
        print(f"Rekisterinumero: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus}, Tämänhetkinen nopeus: {self.tämänhetkinen_nopeus} Kuljettu matka: {self.kuljettu_matka}")


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus,tämänhetkinen_nopeus,kuljettu_matka,kapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus,tämänhetkinen_nopeus,kuljettu_matka)
        self.kapasiteetti = kapasiteetti


    def tulosta(self):
        super().tulosta()
        print(f" Akkukapasiteetti: {self.kapasiteetti}")

class Polttomoottoriauto(Auto):
    def __init__(self,rekisteritunnus, huippunopeus,tämänhetkinen_nopeus,kuljettu_matka,bensatankki):
        super().__init__(rekisteritunnus, huippunopeus, tämänhetkinen_nopeus,kuljettu_matka)
        self.bensatankki = bensatankki

    def tulosta(self):
        super().tulosta()
        print(f" Akkukapasiteetti: {self.bensatankki}")



kaikki = []

kaikki.append(Sähköauto("ABC-15",180, 55, 0,52.5))
kaikki.append(Polttomoottoriauto("ACD-123",165,50,0,32.3))

for auto in kaikki:
    auto.Aja(3)


for t in kaikki:
    t.tulosta()