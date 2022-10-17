import json

class Lietotajs:
    def __init__(self, vards, uzvards, vecums, valoda, pieteiksanos_skaits=0):
        self.vards = vards
        self.uzvards = uzvards
        self.vecums = vecums
        self.valoda = valoda
        self.pieteiksanos_skaits = pieteiksanos_skaits

    def lietotaja_apraksts(self):
        print(f"{self.vards},{self.uzvards},{self.vecums},{self.valoda}")

    def sasveicinies(self):
        print (f"Esi sveicināts/a {self.vards} {self.uzvards}")

    def palielinat_pieteiksanos_skaitu(self):
        self.pieteiksanos_skaits = self.pieteiksanos_skaits+1

    def atiestatit_pieteiksanos_skaitu(self):
        self.pieteiksanos_skaits = 0

nikola = Lietotajs ("Nikola", "Skuja", 17, "latviešu")
druvis = Lietotajs ("Druvis", "Liepa", 34,"angļu")
mudite = Lietotajs ("Mudīte", "Gulbe", 67, "krievu")
nikola.lietotaja_apraksts()
druvis.lietotaja_apraksts()
mudite.lietotaja_apraksts()
nikola.sasveicinies()
druvis.sasveicinies()
mudite.sasveicinies()
nikola.palielinat_pieteiksanos_skaitu()
nikola.palielinat_pieteiksanos_skaitu()
nikola.palielinat_pieteiksanos_skaitu()
nikola.palielinat_pieteiksanos_skaitu()
nikola.palielinat_pieteiksanos_skaitu()
print(nikola.pieteiksanos_skaits)
nikola.atiestatit_pieteiksanos_skaitu()
print(nikola.pieteiksanos_skaits)

class Privilegijas:
    def __init__(self):
        self.privilegijas = ["var pievienot ierakstu", "var dzēst lietotāju", "var dzēst pierakstu", "var pievienot lietotāju"]

    def paradit_privilegijas(self):
        print(f"Privilēģijas: {self.privilegijas}")

class Admin(Lietotajs):
    def __init__(self, vards, uzvards, vecums, valoda, pieteiksanos_skaits=0):
        super().__init__(vards, uzvards, vecums, valoda, pieteiksanos_skaits=0)
        self.privilegijas = Privilegijas()

    def paradit_privilegijas(self):
        print(f"{self.privilegijas}")

    def saglabat_json(self):
        dati = self.veido_vardnicu()
        datiJSON = json.dumps(dati)
        nosauk = f"{self.razotajs}-{self.modelis}-{self.gads}"
        with open("auto.json", "w", encoding="utf-8") as f:
            f.write(datiJSON)

katrina = Admin("Katrīna", "Ločmele", "17", "latviešu")
#katrina.paradit_privilegijas()
print(katrina.privilegijas.paradit_privilegijas())



