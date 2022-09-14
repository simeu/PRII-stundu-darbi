#######
# OOP #
#######

# 16a Doti četri mēģinājumi izveidot klasi "grāmata"
# (2) Atstāj tikai pareizo, pārējos ieliec kā komentāru, pāris vārdos pamatojot, kāpēc tie ir nepareizi

# Class gramata: - "class" nesāk ar lielo sākumburtu
    # def __init__ (self):
        # pass

class Gramata:
    def __init__ (self, nosaukums, autors):
        self.nosaukums = nosaukums
        self.autors = autors

    def paradit(self):
        self.nosaukums = "Sniegbaltīte"
        self.autors = "Maigonis"
        print(f"Nosaukums: {self.nosaukums} Autors: {self.autors}")
        
    paradit(self)

# class gramata:
    # def __init__ (self):


# def gramata: - šī nav klases izveidošana, bet gan funkcija. Apmainīta secība.
    # class __init__ (self):
        # pass

# (1) 16b papildini klases konstruktoru ar jaunu īpašību nosaukums
# (2) 16c izveido metodi paradit, kura parāda grāmatas nosaukumu
# (1) 16d izveido objektu mana_gramata ar Tevis izvēlētu nosaukumu


# 16e noņem komentāru nākamajai rindai un pārbaudi, vai programma parāda grāmatas nosaukumu
# mana_gramata.paradit()