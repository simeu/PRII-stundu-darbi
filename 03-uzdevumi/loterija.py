import random 

loterija_nr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
loterija_br = ["a", "b", "c", "d", "e"]

def loterija():
    print(random.choice(list(loterija_nr)))
    print(random.choice(list(loterija_nr)))
    print(random.choice(list(loterija_nr)))
    print(random.choice(list(loterija_nr)))
    print(random.choice(list(loterija_br)))

loterija()

def loterija_analize():
    mana_bilete = [6, 9,"B", 1]
    