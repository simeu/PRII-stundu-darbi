def pirmais_uzd():
    naturali = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    naturali_kvadrata = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    naturali.append(naturali_kvadrata)
    for x in naturali:
        print(x)
pirmais_uzd()

def otrais_uzd():
    naturali = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, len(naturali)):
         ak = naturali[i] ** 2
         naturali.append(ak)
         print(naturali)

otrais_uzd()
