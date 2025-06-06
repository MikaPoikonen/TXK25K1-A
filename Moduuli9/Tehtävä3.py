#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt
# . Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus = 0, tämänhetkinen_nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self,luku:int):
        self.tämänhetkinen_nopeus += luku
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus

        elif self.tämänhetkinen_nopeus < 0:
             self.tämänhetkinen_nopeus = 0

    def kulje(self,tuntia:float):
        self.kuljettu_matka += tuntia * self.tämänhetkinen_nopeus

def main():
    uusi_auto = Auto("ABC-123", 142)
    uusi_auto.kiihdytä (+ 30)
    uusi_auto.kiihdytä(+ 50)
    uusi_auto.kiihdytä(+ 70)
    uusi_auto.kulje(3)
    print("Rekisteritunnus: ",uusi_auto.rekisteritunnus,"Huippunopeus:", uusi_auto.huippunopeus,"Tämänhetkinen nopeus: ", uusi_auto.tämänhetkinen_nopeus,"Kuljettu matka: ", uusi_auto.kuljettu_matka)

    uusi_auto.kiihdytä(-200)
    print ("Tämänhetkinen nopeus:",uusi_auto.tämänhetkinen_nopeus)

main()