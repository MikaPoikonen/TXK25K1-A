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
kaikki.append(Julkaisu("Karkkikirja"))
kaikki.append(Kirja("Keittokirja", "Martti Servo", 178))
kaikki.append(Lehti("Tintti", "John Wicked"))

for t in kaikki:
    t.tulosta_tiedot()


