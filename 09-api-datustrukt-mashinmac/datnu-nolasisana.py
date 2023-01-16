import csv
import json

def pirmais(datnesnosaukums, garums):
    try:
        with open(datnesnosaukums, "r", encoding="utf-8") as f:
            pasaka = f.read()
        print(pasaka)
        sk = len(pasaka)
        print(f"Simbolu skaits teksta failā: {sk}.")
        desmit = pasaka[0 : 10]
        print(f"Pirmie desmit simboli ir '{desmit}'.")
        pirmais = pasaka[0]
        print(f"Pirmais simbols ir '{pirmais}'.")
        pedejais = pasaka[len(pasaka) -1]
        print(f"Pēdējais simbols ir '{pedejais}'.")
        fragments = pasaka[0:garums]
        print(fragments)
    # ievade = int(input("Ievadiet jebkādu skaitlisku vērtību.")

    except FileNotFoundError:
        print(f"Datne {datnesnosaukums} nav atrasts")
    except TypeError:
        print("Kāds no ievades datiem nav korekts")
    
    finally:
        print("Viss izdarīts.")

def pirmarinda(datnesnosaukums):
    with open(datnesnosaukums, "r", encoding="utf-8")as f:
        teksts = f.read()
        print(teksts.splitlines()[0])

pirmarinda("balta-pasaka.txt")


pirmais("balta-pasaka.txt", 20)
