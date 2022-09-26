class Restorans:
    def __init__(self, restorana_nosaukums, virtuves_tips, apkalpoto_skaits=0):
        self.restorana_nosaukums = restorana_nosaukums 
        self.virtuves_tips = virtuves_tips
        self.apkalpoto_skaits = apkalpoto_skaits

    def restorana_apraksts(self):
        print(f"Restorāna nosaukums ir {self.restorana_nosaukums}, un tam ir {self.virtuves_tips}")

    def restorans_atverts(self):
        print (f"Restorāns \"{self.restorana_nosaukums}\" ir atvērts")

    def iestatit_apkalpoto_skaitu(self, skaits):
        self.apkalpoto_skaits = skaits
        print(f"{self.apkalpoto_skaits}")

    def palielinat_apkalpoto_skaitu(self, skaits):
        if skaits<0:
            print("Tā nevar!")
        else:
            self.apkalpoto_skaits += skaits
        print(f"Dienā apkalpoto cilvēku skaits - {self.apkalpoto_skaits}")

# restorans1 = Restorans("Kuhnja", "franču virtuve")
# print(restorans1.restorana_nosaukums, restorans1.virtuves_tips, restorans1.apkalpoto_skaits)
# restorans1.restorans_atverts()
# restorans1.restorana_apraksts()
# restorans2 = Restorans("Eleon", "itāļu virtuve")
# restorans3 = Restorans("Grand", "spāņu virtuve")
# restorans2.restorana_apraksts()
# restorans3.restorana_apraksts()
# restorans1.iestatit_apkalpoto_skaitu(5)
# restorans1.palielinat_apkalpoto_skaitu(7)

class SaldejumaKiosks(Restorans):
    def __init__(self, restorana_nosaukums, virtuves_tips, apkalpoto_skaits=0):
        super().__init__(restorana_nosaukums, virtuves_tips, apkalpoto_skaits=0)
        saldejuma_garsas = ["vaniļas", "zemeņu", "šokolādes", "riekstu"]
        self.garsas = saldejuma_garsas
    
    def garsas_paradit(self):
        print(f"{self.garsas}")

mans = SaldejumaKiosks("Gelato", "itāļu")
mans.garsas_paradit()