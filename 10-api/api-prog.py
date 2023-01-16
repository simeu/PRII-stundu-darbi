'''import requests
import json

saite = "https://api.open-meteo.com/v1/forecast?latitude=56.95&longitude=24.11&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,precipitation,rain,showers,snowfall,snow_depth&timezone=auto"

r = requests.get(saite)
teksts = r.text
teksts_dict = json.loads(teksts)
# print(teksts_dict)

laikapstakli = teksts_dict["hourly"]
print(laikapstakli)

for katra in laikapstakli:
    print(katra["time"])
    print(katra["temperature_2m"])
    print(katra["relativehumidity_2m"])
    print(katra["dewpoint_2m"])
    print(katra["apparent_temperature"])
    print(katra["precipitation"])
    print(katra["rain"])
    print(katra["showers"])
    print(katra["snowfall"])
    print(katra["snow_depth"])
    print()    

'''

#Copilot/ChatGPT risinājums, jo iepriekšējais kods neiet:
import requests
import json

saite = "https://api.open-meteo.com/v1/forecast?latitude=56.95&longitude=24.11&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,precipitation,rain,showers,snowfall,snow_depth&timezone=auto"

r = requests.get(saite)
if r.status_code != 200:
    raise ValueError(f"Invalid status code: {r.status_code}")

teksts_dict = r.json()
# print(teksts_dict)

# Checking if the returned json has the 'hourly' key
if "hourly" not in teksts_dict:
    raise ValueError(f"The returned JSON doesn't contain the 'hourly' key")

laikapstakli = teksts_dict["hourly"]

'''
for katra in laikapstakli:
    # Checking if the each element of 'hourly' is a dictionary
    if not isinstance(katra, dict):
        raise ValueError(f"The element {katra} is not a dictionary")
        
    print(katra["time"])
    print(katra["temperature_2m"])
    print(katra["relativehumidity_2m"])
    print(katra["dewpoint_2m"])
    print(katra["apparent_temperature"])
    print(katra["precipitation"])
    print(katra["rain"])
    print(katra["showers"])
    print(katra["snowfall"])
    print(katra["snow_depth"])
    print()

'''