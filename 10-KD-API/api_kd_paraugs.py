#1.daļa - API
#Programmsaskarne jeb API https://timeapi.io bez reģistrācijas un API atslēgas var parādīt dažādu informāciju par pareizu laiku dažādās vietās.
# Piemēram, šis vaicājums atgriež informāciju par pareizu laiku Rīgā: https://timeapi.io/api/Time/current/zone?timeZone=Europe/Riga
# Lasi API dokumentāciju https://timeapi.io/swagger/index.html un izveido programmu, kura iegūst sarakstu ar visām laika zonām. No sarakstā atlasi tikai Eiropu.
# Ekrānā stabiņā citu zem citas parādi:
# tikai Eiropas laika zonas pilsētas, kuras sākas ar burtu B,
# pēdējās 5 saraksta pilsētas,
# pirmo saraksta pilsētu.

# * Nodrošini lietotājam ievadīt pilsētas nosaukumu un ekrānā parādi, vai šī pilsēta ir Eiropas laika zonā.

import requests, json

url = "https://timeapi.io/api/TimeZone/AvailableTimeZones" 
r = requests.get(url)
teksts = r.text
teksts_dict = json.loads(teksts)

print(teksts_dict)
tikai_Eiropa = []
for katra in teksts_dict:
    if "Europe" in katra:
        print(katra)
        tikai_Eiropa.append(katra)


# for katra in teksts_dict:
#     if "Europe" in katra and katra[7] == "B":
#         print(katra[7:])
            
tikai_B = []
for katra in tikai_Eiropa:
    if katra.split("/")[1].startswith("B"):
        tikai_B.append(katra)
print(tikai_B)

for katra in tikai_B:
    print(katra.split("/")[1])

for katra in teksts_dict[-5:]:
    if "/" in katra:
        print(katra.split("/")[1])
    else:
        print(katra)
    
print(teksts_dict[0].split("/")[1])

ievade = input("Ievadi pilsētas nosaukumu: ")
for katra in tikai_Eiropa:
    if ievade in katra:
        print(f"{ievade} ir Eiropas laika zonā")
        break
else:
    print(f"{ievade} nav Eiropas laika zonā")


#2.a daļa - Datu struktūras
# Papildini 2. uzdevuma atrisinājumu lai katra punkta atbilde būtu ierakstīta vārdnīcā, kā arī:
# lietotājs var ievadīt jebkādu vārdu un tiek parādīts, vai un cik reizes tas atkārtojas
# programma nosaka vārdu garumu tekstā, saskaita, cik un kāda garuma vārdi ir

# # 2. uzdevums
# #Ielasi datnes balta-pasaka.txt saturu un nosaki
# #cik kuras pieturzīmes ir sastopamas tekstā,
# #cik reizes tekstā parādās vārds balts jebkurā locījumā,
# #cik reizes tekstā atkārtojas kurš vārds.
def ielasit():
    with open("balta-pasaka.txt", "r", encoding="utf-8") as f:
        ielasit = f.read()
        # print (f"Teksts ir {ielasit}")
        return ielasit

#pieturzīmes ir ., !, ?, :, ;, -, —, (, ), „, “, ‘, ’, …
def pieturzimes(ielasit):
    pieturzimes = 0
    for viens in ielasit:
        if viens in ".!?:;-—()„“‘’…,":
        #if viens == "." or viens == "!" or viens == "?" or viens == ":" or viens == ";" or viens == "-" or viens == "—" or viens == "(" or viens == ")" or viens == "„" or viens == "“" or viens == "‘" or viens == "’" or viens == "…":
            pieturzimes += 1
    print (f"Pieturzīmes ir {pieturzimes}")
    return pieturzimes
    # pieturzimes = string.punctuation
    # for zime in pieturzimes:
    #    print (f"{zime}: {ielasit.count(zime)}")

def balts(ielasit):
    # balts = 0

    cik = ielasit.count("balt")
    cik2 = ielasit.count("Balt")


    # for viens in ielasit:
    #     if viens == "b" or viens == "B":
    #         if ielasit[ielasit.index(viens) + 1] == "a" or ielasit[ielasit.index(viens) + 1] == "A":
    #             if ielasit[ielasit.index(viens) + 2] == "l" or ielasit[ielasit.index(viens) + 2] == "L":
    #                 if ielasit[ielasit.index(viens) + 3] == "t" or ielasit[ielasit.index(viens) + 3] == "T":
    #                     if ielasit[ielasit.index(viens) + 4] == "s" or ielasit[ielasit.index(viens) + 4] == "S":
    #                         balts += 1
    print (f"Vārds balts ir {cik + cik2} reizes")

def vardi(ielasit):
#     #nosaki cik reizes tekstā atkārtojas kurš vārds
#     #bez pieturzīmēm un bez lielajiem burtiem
    vardi = {}
    ielasit = ielasit.replace(".", "")
    ielasit = ielasit.replace(",", "")
    ielasit = ielasit.replace("!", "")
    ielasit = ielasit.replace("?", "")
    ielasit = ielasit.replace(":", "")
    ielasit = ielasit.replace(";", "")
    ielasit = ielasit.replace("-", "")
    ielasit = ielasit.replace("—", "")
    ielasit = ielasit.replace("(", "")
    ielasit = ielasit.replace(")", "")
    ielasit = ielasit.replace("„", "")
    ielasit = ielasit.replace("“", "")
    ielasit = ielasit.replace("‘", "")
    ielasit = ielasit.replace("’", "")
    ielasit = ielasit.replace("…", "")
    ielasit = ielasit.lower()
    ielasit = ielasit.split()
    for viens in ielasit:
        if viens not in vardi:
            vardi[viens] = 1
        else:
            vardi[viens] += 1
    print(vardi)
    return vardi



# ielasit()
# pieturzimes(ielasit())
# balts(ielasit())
# vardi(ielasit())

atbilde = {}
atbilde["pieturzimes"] = pieturzimes(ielasit())
atbilde["balts"] = balts(ielasit())
atbilde["vardi"] = vardi(ielasit())
print(atbilde)

def vards():
    vards = input("Ievadi vārdu: ")
    if vards in atbilde["vardi"]:
        print (f"Vārds {vards} ir {atbilde['vardi'][vards]} reizes")
    else:
        print (f"Vārds {vards} nav")

vards()

def garums():
    garums = {}
    for vards in atbilde["vardi"]:
        if len(vards) not in garums:
            garums[len(vards)] = 1
        else:
            garums[len(vards)] += 1
    print(garums)

garums()

#2.b daļa - Datu struktūras
#skatīt catan.py

