class Julkaisu():

    def __init__(self,nimi):
        self.nimi=nimi


    def tulosta_tiedot(self):
        print(f"Julkaisun nimi {self.nimi}")

class Kirja(Julkaisu):

    def __init__(self,nimi,kirjoittaja,sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja} kirjan sivumäärä: {self.sivumäärä}")

class Lehti(Julkaisu):
    def __init__(self,nimi,päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Lehden päätoimittaja: {self.päätoimittaja}")


kaikki = []
kaikki.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))
kaikki.append(Lehti("Aku.Ankka", "Aki Hyyppä"))

for t in kaikki:
    t.tulosta_tiedot()


