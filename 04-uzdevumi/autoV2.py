from datetime import datetime
sodien = datetime.now()
import json

class Auto:
    def __init__ (self, razotajs, modelis, cena, gads, iegades_datums, nobraukums = 0):
        self.razotajs = razotajs
        self.modelis = modelis
        self.cena = cena
        self.gads = gads
        self.iegades_datums = iegades_datums
        self.nobraukums = nobraukums
        self.lietosanas_ilgums = self.noteikt_ilgumu()

    def noteikt_ilgumu(self):
         sodien = datetime.now()
         iegadats = datetime.strptime(self.iegades_datums, "%Y-%m-%d")
         self.ilgums = (sodien - iegadats).days
         return self.ilgums

    def paradit(self):
        # print(f'{self.razotajs} {self.modelis} {self.cena} {self.gads} {self.nobraukums} {self.lietosanas_ilgums}')
        return f'{self.razotajs} {self.modelis} {self.cena} {self.gads} {self.nobraukums} {self.lietosanas_ilgums}'

    def palielinat_nobraukumu(self, km):
        if km < 0:
            print("Tā nevar!")
        else:
            self.nobraukums += km

    def iestatit_nobraukumu(self, km):
        self.nobraukums = km

    def ieliet_degvielu(self):
        print(f'Degviela ir ielieta')

    def veido_vardnicu(self):
        dati = self.__dict__
        return dati

    def saglabat_json(self):
        dati = self.veido_vardnicu()
        datiJSON = json.dumps(dati)
        nosauk = f"{self.razotajs}-{self.modelis}-{self.gads}"
        with open("auto.json", "w", encoding="utf-8") as f:
            f.write(datiJSON)

    def saglabat(self):
        dati = self.paradit()
        with open("auto.txt", "w", encoding = "utf-8") as f:
            f.write(dati)