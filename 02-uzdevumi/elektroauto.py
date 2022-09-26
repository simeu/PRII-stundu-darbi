from auto import Baterija
from auto import ElektroAuto

class Baterija:
    def __init__(self, jauda=100):
        self.jauda = jauda

    def paradit_bateriju(self):
        print(f"Baterija: {self.jauda}")

class ElektroAuto(auto):
    def __init__(self, razotajs, modelis, cena, gads, nobraukums=0):
        super().__init__ (razotajs, modelis, cena, gads, nobraukums=0)
        #self.baterija = 123
        self.baterija = Baterija()

