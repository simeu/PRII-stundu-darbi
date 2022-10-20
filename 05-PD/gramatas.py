import json


class Gramata():
    def __init__(self, nosaukums, autors, skaits, cena):
        self.nosaukums = nosaukums
        self.autors = autors 
        self.skaits = skaits
        self.cena = cena
    
    def izvelne():
        print("Labrīt/Labdien/Labvakar! \nŠī ir grāmatu aplikācija, kas ļauj jums sekot līdzi jūsu ienākumiem, grāmatu skaitam, u. tml.")
    
    def paradit(self):
        ievadits = print(f"{self.nosaukums} \n{self.autors}, \n{self.skaits} \n{self.cena}")
        print(ievadits)

    def veido_vardnicu(self):
        dati = self.__dict__
        return dati

    def saglabat():
        dati = json.dumps()
        with open("gramatas.json", "w", encoding="utf-8")as f:
            f.write(dati)