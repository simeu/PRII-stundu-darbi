import hashlib

slepena = "adf94f1009dfc2ddc721812cbead6e9cd2fa89570b1e21fd4d9c66da61ab1574"

def pieslegties():
    print("Sveiki, lūdzu ielogoties!")
    parole = input("Ievadi savu paroli: ")
    parole_bin = str.encode(parole)
    parole_hash = hashlib.sha256(parole_bin)
    parole_hash_virkne = parole_hash.hexdigest()
    if parole_hash_virkne == slepena:
        programma()
    else:
        kluda()

def programma():
    print("Pieslēgšanās veiksmīga, sāc strādāt.")

def kluda():
    print("Nepareiza parole. Mēģini vēlreiz.")
    pieslegties()

pieslegties()

