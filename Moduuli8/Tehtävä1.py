import mysql.connector

def airport(ident):
    sql = f"SELECT name FROM airport where ident='{ident}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)
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
airport(ident)