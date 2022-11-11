import json
from datetime import datetime

class Noma:
    def __init__(self, kategorija, nosaukums, raksturojums, cena, pieejamiba, vards, uzvards, pkods, tel, sakdat, beigdat):
        self.kategorija = kategorija
        self.nosaukums = nosaukums
        self.raksturojums = raksturojums
        self.cena = cena
        self.pieejamiba = pieejamiba
        self.vards = vards
        self.uzvards = uzvards
        self.pkods = pkods
        self.tel = tel
        self.sakdat = sakdat
        self.beigdat = beigdat

    def paradit(self):
        ievadits = print(f"{self.kategorija}, {self.nosaukums}, {self.raksturojums}, {self.cena}, {self.pieejamiba}, {self.vards}, {self.uzvards}, {self.pkods}, {self.tel}, {self.sakdat}, {self.beigdat}")
        print(ievadits)

    def aprekini(self):
        v = self.sakdat
        b = self.beigdat
        atlicis = b-v
        print(f"Jums ir atlikušas {atlicis} dienas līdz nomas beigām.")

    def vardnica(self):
        dati = self.__dict__
        return dati

    def saglaba(self):
        dati = self.vardnica()
        datiJSON = json.dumps(dati)
        with open("noma.json", "w", encoding="utf-8") as f:
            f.write(datiJSON)

 


    



    