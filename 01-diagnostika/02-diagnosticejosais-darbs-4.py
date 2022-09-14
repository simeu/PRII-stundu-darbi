import json
import csv
import sqlite3
import os
from os import listdir
from os.path import isfile, join
conn = sqlite3.connect("lv-filmu-datubaze.db")
c = conn.cursor()
dictObj = []
############################
# Teksta datnes, datubāzes #
############################
# 11. (1) Importē nepieciešamos moduļus (bibliotēkas) darbam ar csv un json datnēm, kā arī sqlite datubāzi
# 12. (2) Atver CSV datni bibliotekas.csv un parādi tās saturu ekrānā
### 13. uzdevuma sākums
# (2) Atver un nolasi JSON datni dzervene.json, lai iegūtu mainīgo ar datu tipu <dict>
def paradisana():
    with open("dzervene.json")as fp:
        dictObj = json.load(fp)
        print(dictObj)

paradisana()

# (1) Papildini vārdnīcu ar jaunu atslēgu-vērtību pāri:
# angliski – cranberry
print(dictObj)

dictObj.update({"angliski": "cranberry"})

print(dictObj)

# (2) papildināto vārdnīcu ieraksti teksta datnē dzervene-labots.json

files = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]

for f in files:
  if f.endswith('.json'):
    openFile=open(f,"r")
    fileData = json.load(openFile)
    oldName = fileData['.json']['dzervene']
    newName = oldName.replace('dzervene-labots.json')
    os.rename(f,newName)
    print(f"Fails nomainīts no {oldName} uz {newName}")


### 13. uzdevuma beigas


# Dota datubāze lv-filmu-datubaze.db
# (DB un tabulas struktūras izpētīšanai izmanto DB Browser)

# 14.
# (1) Uzraksti, cik tabulas ir šajā DB:
# (1) Uzraksti, cik lauki ir tabulā lv_filmas: 
# (1) Uzraksti, cik ieraksti ir tabulā lv_filmas: 

# 15a (1) Izveido savienojumu un kursoru

# 15b (2) Izveido vaicājumu, kurš no tabulas lv_filmas atlasa 2018. gada filmas

# 15c (2) Parādi vaicājuma rezultātu ekrānā
