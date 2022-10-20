import json
# from fpdf import FPDF

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

    def veido_vardnicu(self):
        dati = self.__dict__
        return dati

    def saglabat_json(self):
        dati = self.veido_vardnicu()
        datiJSON = json.dumps(dati)
        nosaukums = f'{self.vards}-{self.uzvards}-{self.valoda}.json'
        with open(nosaukums, "w", encoding="utf-8") as f:
            f.write(datiJSON)

    # def saglabat_pdf(self):
        # pdf = FPDF()
        # pdf.add_page()
        # pdf.set_font("Arial", size=12)
        # pdf.cell(200, 10, txt="Lietotaji", ln=1, align="C")
        # pdf.cell(200, 10, txt="Lietotajvārds: " + self.vards, ln=1, align="L")
        # pdf.cell(200, 10, txt="Vards, Uzvards: " + self.uzvards, ln=1, align="L")
        # pdf.cell(200, 10, txt="Vecums: " + str(self.vecums), ln=1, align="L")
        # pdf.cell(200, 10, txt="Valoda: " + self.valoda, ln=1, align="L")
        # pdf.output("lietotajs.pdf")

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


# katrina = Admin("Katrīna", "Ločmele", "17", "latviešu")
#katrina.paradit_privilegijas()
# print(katrina.privilegijas.paradit_privilegijas())