# sarežģītāks piemērs
import requests
import json

# sarežgītību rada nevis liela, gara atbilde, bet gan vaicājums ar ekstra parametriem
# Piemērs ar mašīntulkotāju deepl

url = "https://api-free.deepl.com/v2/translate"
atslega = "a98ee08d-b72a-a7bc-3e1f-f2442f83f6ef:fx"
uz_ko_tulkot = "DE"
teksts = "kompetenču izglītība"

params = {}
params["auth_key"] = atslega
params["target_lang"] = uz_ko_tulkot
params["text"] = teksts

r = requests.get(url, params)
atbilde = json.loads(r.text)

print(atbilde["translations"][0]["text"])
