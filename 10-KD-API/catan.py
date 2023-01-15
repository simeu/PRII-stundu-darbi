import random


def gajieni():
    spele = []

    for i in range(30):
        k1 = random.randrange(1, 7)
        k2 = random.randrange(1, 7)
        gajiens = [k1, k2]
        spele.append(gajiens)

    spele = [[random.randrange(1, 7), random.randrange(1, 7)] for i in range(30)]
    # print(spele)
    return spele
    
def laupitajs(spele):
    laupitajs = 0
    for gajiens in spele:
        if sum(gajiens) == 7:
            laupitajs += 1
    print (f"Laupītājs atnāca {laupitajs} reizes")
    return laupitajs

gajieni()
laupitajs(gajieni())

def summa(spele):
    summa6 = 0
    summa8 = 0
    for gajiens in spele:
        if sum(gajiens) == 6:
            summa6 += 1
        elif sum(gajiens) == 8:
            summa8 += 1
    print (f"Summa 6 atnāca {summa6} reizes")
    print (f"Summa 8 atnāca {summa8} reizes")
    return summa6, summa8

summa(gajieni())

def summa2(spele):
    summa2 = 0
    summa12 = 0
    for gajiens in spele:
        if sum(gajiens) == 2:
            summa2 += 1
        elif sum(gajiens) == 12:
            summa12 += 1
    print (f"Summa 2 atnāca {summa2} reizes")
    print (f"Summa 12 atnāca {summa12} reizes")
    return summa2, summa12

summa2(gajieni())