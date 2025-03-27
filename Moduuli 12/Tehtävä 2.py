import requests

api =""
kaupunki = input("Anna kaupunki")

osoite = f"http://api.openweathermap.org/geo/1.0/direct?q={kaupunki}&limit=5&appid={api}"

def celsius (lampotila:float):
            lampotila = lampotila - 273.15
            return lampotila

try:
    vastaus = requests.get(osoite)

    data = vastaus.json()
    if len(data) > 0:
        lat=(data[0]["lat"])
        lon=(data[0]["lon"])
        osoite2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"
        vastaus2 = requests.get(osoite2)
        data2 = vastaus2.json()
        if len(data2["weather"]) > 0:

            print(data2["weather"][0]["main"])
        lampotila = celsius(data2["main"]["temp"])
        print(f"Lämpötila  on: {lampotila:.2} astetta")

    else:
        print("Väärä kaupunki")

except requests.exceptions.RequestException as e:
    print(" Haku ei onnistunut LOL")