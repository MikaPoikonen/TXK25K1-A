class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus = 0, kuljettu_matka = 0):
        Auto.rekisteritunnus = rekisteritunnus
        Auto.huippunopeus = huippunopeus
        Auto.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        Auto.kuljettu_matka = kuljettu_matka

Auto1 =Auto("ABC-123",142)
print("Rekisteritunnus", Auto.rekisteritunnus, "Huippunopeus", Auto.huippunopeus, "Tämänhetkinen nopeus", Auto.tämänhetkinen_nopeus, "Kuljettu matka", Auto.kuljettu_matka)