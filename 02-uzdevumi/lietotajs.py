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

simona = Lietotajs ("Simona", "Baumane", 18, "latviešu")
maris = Lietotajs ("Māris", "Lielpēdis", 34,"krievu")
mudite = Lietotajs ("Mudīte", "Spriņģe", 67, "angļu")
simona.lietotaja_apraksts()
maris.lietotaja_apraksts()
mudite.lietotaja_apraksts()
simona.sasveicinies()
maris.sasveicinies()
mudite.sasveicinies()
simona.palielinat_pieteiksanos_skaitu()
simona.palielinat_pieteiksanos_skaitu()
simona.palielinat_pieteiksanos_skaitu()
simona.palielinat_pieteiksanos_skaitu()
simona.palielinat_pieteiksanos_skaitu()
print(simona.pieteiksanos_skaits)
simona.atiestatit_pieteiksanos_skaitu()
print(simona.pieteiksanos_skaits)

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

katrina = Admin("Katrīna", "Lielpēde", "35", "latviešu")
#katrina.paradit_privilegijas()
print(katrina.privilegijas.paradit_privilegijas())

