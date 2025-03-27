import requests
import json


osoite = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(osoite)

    data = vastaus.json()

    #print(json.dumps(data, indent=2))
    print(data["value"])
except requests.exceptions.RequestException as e:
    print(" Haku ei onnistunut LOL")