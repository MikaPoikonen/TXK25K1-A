#Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan
#lentokentän nimen ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
#Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
#Vastauksen on oltava muodossa:
#{"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True,
    collation='utf8mb3_unicode_ci'
)

app = Flask(__name__)
@app.route('/kenttä/<ICAO>')

def kenttä(ICAO):




    sql = f"SELECT ident, name, municipality from airport where ident ='{ICAO}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return  {"ICAO":tulos[0][0], "Name":tulos[0][1], "Municipality":tulos[0][2]}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
