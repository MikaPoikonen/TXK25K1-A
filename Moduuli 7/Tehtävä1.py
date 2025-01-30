vuodenajat = {"1":"Talvi",
              "2":"Talvi",
              "3":"Talvi",
              "4":"Kevät",
              "5":"Kevät",
              "6":"Kevät",
              "7":"Kesä",
              "8":"Kesä",
              "9":"Kesä",
              "10":"Syksy",
              "11":"Syksy",
              "12":"Syksy",}

kuukausi = input("Anna kuukausi: ")
if kuukausi in vuodenajat:
     print (f"Kuukausi {kuukausi}  on {vuodenajat[kuukausi]}.")