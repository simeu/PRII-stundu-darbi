# visvienkāršākais piemērs

import requests # modulis, lai varētu atvilkt datus no API
import json # visdrīzāk API atbildes teksts būs JSON formāta, tāpēc arī šis

saite = "https://catfact.ninja/fact" # API saite. Skolotāja dota, internetā atrasta utt.

r = requests.get(saite) # iegūstam atbildi

status = r.status_code
print(status)
teksts = r.text # no atbildes izvelkam tekstu
print(teksts)

# Tā kā atbilde ir acīmredzami vārdnīcas struktūrā, tad jāpiestrādā pie rezultāta parādīšanas
teksts_dict = json.loads(teksts)
atslega = "fact"
print(f"Kāds fakts par kaķiem: {teksts_dict[atslega]}")