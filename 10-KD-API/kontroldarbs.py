import requests
import json

# 1. uzdevums.

url = "http://universities.hipolabs.com/search?name=university"
req = requests.get(url)
teksts = req.text
teksts_dict = json.loads(teksts)
# print(teksts_dict)

def pirmais_punkts():
    lietuva = []
    for katra in teksts_dict:
        if "Lithuania" in katra["country"]:
            lietuva.append(katra)
            print(lietuva)

# pirmais_punkts()

def otrais_punkts():
    universitates = []
    for katra in teksts_dict:
        if "university" or "University" in katra["name"]:
            universitates.append(katra)
            kartots = sorted(universitates, key=lambda x: x["name"])
            print(kartots)

# otrais_punkts()

def tresais_punkts():
        universitates = []
        for katra in teksts_dict:
            if "university" or "University" in katra["name"]:
                universitates.append(katra)
                uni = print(universitates)
                for line in uni:
                    print(line.split("\n")) # "TypeError: "NoneType" object is not iterable"

# tresais_punkts()

#2. uzdevums.

def ielasit():
    with open("teksts.txt", "r", encoding="utf-8") as f:
        teksts = f.read()
        return teksts

# ielasit()

def vardi():
    for viens in ielasit:
        if viens not in vardi:
            vardi[viens] = 1
        else:
            vardi[viens] += 1
    print(vardi)
    return vardi #"TypeError: 'function' object is not subscriptable"

# vardi()



    