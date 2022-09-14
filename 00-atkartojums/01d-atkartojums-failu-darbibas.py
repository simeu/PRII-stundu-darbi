# Dotas datnes epakalpojumi.csv un pancakes.json
# Vismaz vienu no tiem atver un nolasi, izmantojot piemērotu moduli. Nolasīto saturu parādi Tevis izvēlētā izskatā.
import json
import os

# Dota viena vārdnīca un viens masīvs. Izmantojot piemērotu moduli (bibliotēku), vismaz vienu tiem ieraksti piemērota formāta failā.
oga = {"Nosaukus": "Dzērvene", "Krāsa": "Sarkana", "Augšanas vieta": "Purvs, dārzs"}
darzeni = ["Kartupeļi", "Burkāni", "Bietes", "Kabači", "Kāļi"]

def paradisana():
    with open("pancakes.json", "r", encoding = "utf-8")as fails:
        dati = fails.read()
        print(dati)

paradisana()

def ierakstishana():
    if not os.path.exists("ogas_un_darzeni.json"):
        ediens = ""
        dati = json.dumps(oga, ensure_ascii=False)
        with open ("ogas_un_darzeni.json", "w", encoding = "utf-8") as fails:
            fails.write(dati)

ierakstishana()