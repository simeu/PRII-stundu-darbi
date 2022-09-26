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

