from bs4 import BeautifulSoup
import json
import requests


data = requests.get("https://www.crous-rennes.fr/se-restaurer/ou-manger/").text
state = BeautifulSoup(data,features="html.parser")

liste = []

description = state.find_all("span", {"class": "restaurant_opening_state"})

for item in description :
    nom = item.parent.find("div",{"class":"restaurant_title"}).text
    ouverture = item["data-opening"]

    if "astrolabe" in nom.lower() or "insa" in nom.lower() or "etoile" in nom.lower() :
        liste.append({
            nom:nom,
            ouverture:ouverture
        })

with open("./index.json") as file:
    file.write(json.dumps(liste))
