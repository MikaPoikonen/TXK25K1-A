class Hissi:
    def __init__(self, ylin=5, alin = 0):
        self.ylin = ylin
        self.alin = alin
        self.kerros = 0

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

    def palohälytys(self):
        self.haluttu_kerros = 0
        while self.kerros != self.haluttu_kerros:
            if self.kerros < self.haluttu_kerros:
                self.hissi_ylös()
            if self.kerros > self.haluttu_kerros:
                self.hissi_alas()



hissi1 =Hissi()
print(hissi1.kerros)
hissi1.kerrokseen(5)
hissi1.kerrokseen(2)
hissi1.palohälytys()
print(hissi1.kerros)