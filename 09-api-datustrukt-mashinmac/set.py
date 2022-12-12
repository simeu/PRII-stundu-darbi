# "Set" uzdevumi.

def otrais():
    pari = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50}
    pari2 = {52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100}
    pari3 = pari|pari2
    print(pari3)

otrais()

def tresais():
    x1 = 0
    x2 = 1
    n = int(input("Ievadiet skaitli no 1-20: "))
    xn = 2*(n) - 1 + (n) - 2
    # rezultati = {}
    # x = rezultati.add(xn) #neiet kods?
    print(xn)

tresais()

def ceturtais():
    pass