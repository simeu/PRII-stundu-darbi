import random

class Kaulins:
    def __init__(self, skaldne = 6):
        self.skaldne = skaldne

    def mest_kaulinu(self):
        return random.randint(1, self.skaldne+1)

k10 = Kaulins(10)
rezultati = []
for i in range(10):
    rezultati.append(k10.mest_kaulinu())
print(rezultati)

k20 = Kaulins(20)
rezultati1 = []
for i in range(20):
    rezultati1.append(k20.mest_kaulinu())
print(rezultati1)

    
