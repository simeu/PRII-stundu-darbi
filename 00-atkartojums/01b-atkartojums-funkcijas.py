import math 
a = 21
b = 7

# Nodefinē funkcju pirma() bez parametriem
# Funkcijai jāparāda a un b summa

def pirma():
    int(print(a+b))

# Nodefinē funkciju otra() ar diviem parametriem c un d
# Funkcijai jāatgriež abu parametru starpība --- return

def otra():
    c = 7
    d = 8
    atbilde = int(print(a-b))
    return atbilde

# Izsauc funkciju pirma()
pirma()

# Izsauc funkciju otra() ar a un b kā parametriem
otra(a, b)

# Izsauc funkciju otra() ar diviem Tevis izvēlētiem skaitļiem kā parametriem
otra(a = 4,b = 6)

# Izveido funkciju tresa() bez parametriem
# tai jāizsauc funkcija otra() ar diviem Tevis izvēlētiem skaitļiem kā parametriem un rezultāts jāsaglabā mainīgajā e
def tresa():
    otra(a = 4, b = 6)
    int(print(a+b))

# Mainīgā e vērtība jāparāda