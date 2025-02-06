import mysql.connector

def airport(iso_country):
    sql = f"SELECT type FROM airport where iso_country='{iso_country}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)
    sanakirja={}
    for i in tulos:
        if i not in sanakirja:
            sanakirja[i]=1
        else:
            sanakirja[i]+=1
    print(sanakirja)

yhteys=mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='mika',
    password='tieto',
    autocommit=True,
    collation='utf8mb3_general_ci'
    )
iso_country = input("Anna koodi: ")
airport(iso_country)