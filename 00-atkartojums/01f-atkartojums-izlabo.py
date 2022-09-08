import random
import math
# jāparāda uzrakstu "Programmēšana II"
def pirma():
    print("Programmēšana II")

# Jāparāda uzraksti "Labi", "Izcili" vai "cits vērtējums", atkarībā no parametrā iedotā skaitļa
def otra(atzime):
    a = ""
    if a == 7:
        print("Labi")
    elif a == 10:
        print("Izcili")
    else:
        print("Cits vērtējums")
# Jāparāda stabiņā skaitļi no 1 līdz 10
def tresa():
    for i in range(1, 11):
        print(i)

# Jāparāda stabiņā uz leju masība mas ieraksti
def ceturta():
    mas = [9, 6, 7, 3, 4, 10, 7]
    nr = 1
    for viens in mas:
        print(f"{nr} {mas}")
        nr = nr+1

# Jāparāda nejaušu skaitli starp 0 un 1
def piekta(): 
    print(random.random())

# jāparāda parametru a un b reizinājums
def sesta():
    a = int(input("Ievadi naturālu skaitli"))
    b = int(input("Ievadi vēlvienu naturālu skaitli"))
    print(a*b)

# jāizsauc funkcija pirma
def septita():
    pirma()