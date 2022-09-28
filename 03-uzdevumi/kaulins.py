import random

class Kaulins:
    def __init__(self, skaldne):
        self.skaldne = skaldne

    skaldne1 = 6
    skaldne2 = 10
    skaldne3 = 20

    def mest_kaulinu(skaldne1, skaldne2, skaldne3):
        nr = random.randint(1, skaldne1)
        print(nr)
        nr2 = random.randint(1, skaldne2)
        print(nr2)
        nr3 = random.randint(1, skaldne3)
        print(nr3)

    mest_kaulinu(skaldne1, skaldne2, skaldne3)

    
