from datetime import datetime
# from fpdf import FPDF

sodien = datetime.now()

class Auto:
    def __init__ (self, razotajs, modelis, krasa, gads, nobraukums, cena):
        self.razotajs = razotajs
        self.modelis = modelis
        self.krasa = krasa
        self.gads = gads
        self.nobraukums = nobraukums
        self.cena = cena

    def paradit(self):
        print(f"{self.razotajs} {self.modelis} {self.krasa} {self.gads} {self.nobraukums} {self.cena}")

    def veido_vardnicu(self):
        auto_dict = self.__dict__
        return auto_dict

    def saglabat_json(self):
        dati = self.veido_vardnicu()
        dati_json = json.dumps(dati, ensure_ascii=False)
        with open("auto.json", "w", encoding="utf-8") as f:
            f.write(dati_json)

    def saglabat(self):
        dati = self.paradit()
        with open("auto.txt", "w", encoding="utf-8") as f:
            f.write(dati)
