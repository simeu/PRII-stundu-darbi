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
    pass

def ceturtais():
    pass

