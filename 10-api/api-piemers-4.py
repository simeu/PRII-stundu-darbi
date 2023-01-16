# sarežģītāks piemērs
import requests
import json

# sarežgītību rada nevis liela, gara atbilde, bet gan vaicājums ar ekstra parametriem
# Piemērs ar mašīntulkotāju hugo.lv
# tiek izmantots POST nevis GET

url = "https://hugo.lv/ws/Service.svc/json/Translate"
atslega = "u-e5ac5f94-1fdf-40cc-968d-443bf4b8be89"
# uz_ko_tulkot = "EN"
teksts = "Laimīgu jauno gadu!"
appID = "r6vs"
systemID = "smt-e98a9ae8-c288-45bb-bbe2-0cf0baf3019d"

head = {}
head["client-id"] = atslega

params = {}
params["systemID"] = systemID
params["text"] = teksts
params["appId"] = appID

# šis bija vajadzīgs, lai noskaidrotu sistēmas ID
#rID = requests.get("https://hugo.lv/ws/Service.svc/json/GetSystemList?appID=myapp", headers=head)
#print(rID.text)

r = requests.post(url, headers=head, json=params)
status = r.status_code
atbilde = r.text

print(atbilde)
