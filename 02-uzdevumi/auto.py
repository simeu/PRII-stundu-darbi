class Auto:
    def __init__(self, razotajs, modelis, cena, gads, nobraukums=0):
        self.razotajs = razotajs
        self.modelis = modelis
        self.cena = cena
        self.gads = gads
        self.nobraukums = nobraukums

    def paradit(self):
        print(f"{self.razotajs} {self.modelis} {self.cena} {self.gads} {self.nobraukums}")

    def palielinat_nobraukumu(self, km):
        if km<0:
            print("Tā nevar!")
        else:
            self.nobraukums += km

    def ieliet_degvielu(self):
        print(f"Degviela ir ielieta")


    def ieliet_degvielu(self):
        print("Nav aktuāli")

pirmais = Auto("BMW", "345", 30000, 2022)
pirmais.paradit()
pirmais.palielinat_nobraukumu(1000)
pirmais.paradit()

otrais = Auto("Audi", "A4", 31000, 2021, 5)
otrais.paradit()
otrais.palielinat_nobraukumu(-500)
otrais.paradit()

# tresais = ElektroAuto("Tesla", "Model X", 121000, 2022)
# tresais.paradit()
# print(tresais.baterija.paradit_bateriju())
# tresais.ieliet_degvielu()