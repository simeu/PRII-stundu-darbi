# standarta piemērs

import requests, json

# API https://catfact.ninja/fact atdeva vienu faktu par kaķiem.
# zināms, ka ar /breeds būtu iegūstama informācija par kaķu sugām

# Maini iepriekšējā piemēra API pieprasījumu un ekrānā parādi informāciju par sugām, kuras izveidotas Apvienotajā Karalistē (United Kingdom)

url = "https://catfact.ninja"
parametrs = "/breeds" # šādi dalīt nav obligāti, tomēr, ja garāks pieprasījums, būs pārskatāmāk

saite = url + parametrs

r = requests.get(saite)
teksts = r.text
teksts_dict = json.loads(teksts)

# Ar print un/vai atkļūdotāju iepazīstamies ar saņemto datu struktūru
print(teksts_dict)

# šajā datu kopā redzams, ka mūs interesējoši dati ir atslēgas "data" vērtība. Tas būs masīvs ar vārdnīcām.
# Un šajos masīvos ir vārdnīcas ar atslēgām "breed", "country" un citām. Uzdevums prasa atlasīt noteiktas country vērtības.

sugas = teksts_dict["data"]
tikai_UK = []

for katra in sugas:
    if "United Kingdom" in katra["country"]:
        tikai_UK.append(katra)

# print(tikai_UK)

for katra in tikai_UK:
    for atslega in katra:
        print(f"{atslega} - {katra[atslega]}")
    print()







