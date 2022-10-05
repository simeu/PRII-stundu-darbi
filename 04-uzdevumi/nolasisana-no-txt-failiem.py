with open("piens.txt", "r", encoding="utf=8")as f:
    teksts = f.read()

print(teksts)

with open("stabini.txt", "r", encoding="utf-8") as f:
    teksts = f.readlines()
    print(teksts)

with open("stabini.txt", "r", encoding="utf-8") as f:
    teksts_tirs = []
    for rinda in f:
        teksts_tirs.append(rinda.strip())
    
    print(teksts_tirs)