# Korteža uzdevumi.

def pirmais():
    menesi = ("Janvāris", "Februāris", "Marts", "Aprīlis", "Maijs", "Jūnijs", "Jūlijs", "Augusts", "Septembris", "Oktobris", "Novembris", "Decembris")
    men = menesi.index("Februāris")
    print(men)
    print(menesi[1])

pirmais()

def otrais():
    t = ("a", "b", "c", "d")
    print(t)
    a = reversed(t)
    a = tuple(a)
    print(a)

otrais()
