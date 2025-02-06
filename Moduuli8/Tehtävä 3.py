#Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän
#ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
#Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
#Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
#Asenna kirjasto valitsemalla View / Tool Windows / Python Packages
# . Kirjoita hakukenttään geopy ja vie asennus loppuun.
import geopy.distance
import mysql.connector

import mysql.connector

def airport(ident):
    sql = f"SELECT latitude_deg,longitude_deg FROM airport where ident='{ident}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)
    return tulos

yhteys=mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='mika',
    password='tieto',
    autocommit=True,
    collation='utf8mb3_general_ci'
    )




ident = input("Anna koodi: ")
paikka1=airport(ident)
ident2 = input("Anna toinen kenttä: ")
paikka2=airport(ident2)
erotus = geopy.distance.distance(paikka1, paikka2).kilometers
print(erotus)