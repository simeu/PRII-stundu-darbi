import string

with open("balta-pasaka.txt", "r", encoding="utf-8") as f:
    teksts = f.read()
    print(teksts)

#count = 0

#for i in teksts(0, len(teksts)):
#if teksts[i] in ("!", ".", ",", "?", "-", "_"):
#count = count + 1
#print(f"Pieturzīmju skaits tekstā: {count}")

#for i in teksts:
 #   if i in string.punctuation:
  #      print("Pieturzīme: " + i)
#
 #   skaits = len(string.punctuation)
 #   print(f"Pieturzīmju skaits teksta failā: {skaits}")

pieturzimes = string.punctuation
for zime in pieturzimes:
    if teksts.count(zime) > 0:
        print(f"{zime}: {teksts.count(zime)}")

mazieburti = teksts.lower()

cik = mazieburti.count("balt")
print(f"Vārds 'balts' tekstā parādās {cik} reizes.")
