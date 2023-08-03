from bs4 import BeautifulSoup
import json
import requests


req = requests.get("https://www.crous-rennes.fr/se-restaurer/ou-manger/")

if req.status_code != 200 : raise Exception("Api Univ Pété") 

data = req.text

state = BeautifulSoup(data,features="html.parser")

liste = []

description = state.find_all("span", {"class": "restaurant_opening_state"})

for item in description :
    nom = item.parent.find("div",{"class":"restaurant_title"}).text
    ouverture = item["data-opening"].split(",")

    if "astrolabe" in nom.lower() or "insa" in nom.lower() or "etoile" in nom.lower() :
        liste.append({
            "nom":nom,
            "ouverture":ouverture
        })

with open("./out/index.json","w+") as file:
    file.write(json.dumps(liste))
