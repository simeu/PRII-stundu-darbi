# Vārdnīcu uzdevumi.

def pirmais():
    atzimes = {10: "izcili", 9: "teicami", 8: "ļoti labi", 7: "labi", 6: "gandrīz labi", 5: "viduvēji", 4: "gandrīz viduvēji", 3: "nav labi", 2: "depresīvi", 1:":("}
    atzime = int(input("cik?"))
    print(atzimes[atzime])

pirmais()

def otrais():
    saraksts = [i for i in range(1, 21)]
    print(saraksts)
    kvadrati = [i**2 for i in saraksts]
    print(kvadrati)
    vard = {}
    for i in range(20):
        vard[saraksts[i]] = kvadrati[i]
otrais()

def tresais():
    sk = {}
    for i in range(1, 101):
        sk[i] = sum(range(1, i + 1))
        print(sk)

tresais()


def ceturtais():
    pirmskaitli = {1:2, 2:3, 3:5, 4:7, 5:11, 6:13, 7:17}
    numurs = {}
    for i in pirmskaitli:
        numurs[i] = (pirmskaitli[i], pirmskaitli[i] ** 2)
        print(numurs)

ceturtais()

def piektais():
    tulkojums1 = {0: "nulle", 1: "viens", 2: "divi"}
    tulkojums2 = {3: "trīs", 4: "četri", 5: "pieci"}
    tulkojums3 = {6: "seši", 7: "septiņi", 8: "astoņi"}
    kopaa = {**tulkojums1, **tulkojums2, **tulkojums3}
    print(kopaa)

piektais()



