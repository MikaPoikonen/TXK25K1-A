from random import randint

class Hissi:
    def __init__(self, ylin=5, alin = 0):
        self.ylin = ylin
        self.alin = alin
        self.kerros = alin

    def hissi_ylös(self):
        if self.kerros < self.ylin:
            self.kerros = self.kerros +1
            print(self.kerros)

    def hissi_alas(self):
        if self.kerros > self.alin:
            self.kerros = self.kerros -1
            print(self.kerros)

    def kerrokseen(self,haluttu_kerros):
        while self.kerros != haluttu_kerros:
            if self.kerros < haluttu_kerros:
                self.hissi_ylös()
            if self.kerros > haluttu_kerros:
                self.hissi_alas()


class Talo():
    def __init__(self, hissimaara = 0, alin = 0, ylin=5):
        self.hissimaara = hissimaara
        self.alin = alin
        self.ylin = ylin
        self.hissit = [Hissi(0, randint(1, ylin)) for i in range(hissimaara)]

    def ajahissia(self, hissinumero: int,haluttu):
        self.hissit[hissinumero].kerrokseen(haluttu)

talo=Talo(2,0,5)
print(talo.hissimaara)
talo.ajahissia(1,2)
print(talo.hissit[1].kerros)



