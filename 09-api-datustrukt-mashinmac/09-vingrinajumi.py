# "List" uzdevumi.
def pirmais_uzd():
    naturali = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 16, 25, 36, 49, 64, 81]
    print(naturali)

pirmais_uzd()

def otrais_uzd():
    naturali = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 16, 25, 36, 49, 64, 81]
    sk1 = naturali[0] = 1
    sk2 = naturali[17] = 81
    print(f"Pirmais un pēdējais saraksta loceklis ir {sk1} un {sk2}.")

otrais_uzd()

def tresais_uzd():
    naturali = [0, 1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 16, 25, 36, 49, 64, 81]
    summa = sum(naturali)
    print(f"Skaitļu virknes summa ir {summa}.")

tresais_uzd()

def ceturtais_uzd():
    f1 = 1
    f2 = 1
    n = int(input("Ievadi ciparu no 1-10."))
    fn = (n)-(f1) + (n)-(f2)
    print(f"Iznākums ir {fn}.")

ceturtais_uzd()

def piektais_uzd():
    pilsetas = ["Rīga", "Madona", "Ventspils", "Daugavpils", "Ogre"]
    p = max(pilsetas, key=len)
    print(p)

piektais_uzd()

def sestais_uzd():
    s1 = [2, 4, 6, 8]
    s2 = [10, 12, 14, 16]
    s3 = s1 + s2
    print(s3)

sestais_uzd()

# Korteža uzdevumi.

def pirmais():
    menesi = ("Janvāris", "Februāris", "Marts", "Aprīlis", "Maijs", "Jūnijs", "Jūlijs", "Augusts", "Septembris", "Oktobris", "Novembris", "Decembris")
    men = menesi.index("Februāris")
    print(menesi[1])

pirmais()

def otrais():
    t = ("a", "b", "c", "d")
    print(t)
    a = reversed(t)
    a = tuple(a)
    print(a)

otrais()

#def tresais():


