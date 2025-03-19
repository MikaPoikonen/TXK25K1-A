class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus = 0
        self.kuljettu_matka = kuljettu_matka = 0

def main():
    uusi_auto=Auto("ABC-123",142)
    print("Rekisteritunnus", uusi_auto.rekisteritunnus,"Huippunopeus:",uusi_auto.huippunopeus,"mk/h")
main()