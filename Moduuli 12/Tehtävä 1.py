import requests



osoite = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(osoite)

    data = vastaus.json()

    print(data["value"])
except requests.exceptions.RequestException as e:
    print(" Haku ei onnistunut LOL")