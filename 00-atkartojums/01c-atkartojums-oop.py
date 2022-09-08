# Izveido konstruktoru klasei Suns
# Klasei jābūt ar vienu īpašību vards

class Suns:
    def __init__(self, vards):
        self.vards = vards

suns1 = Suns("Sunītis")
suns2 = Suns("Maigonis")
# konstruktorā izveido šādas darbības (metodes)
# est –– tai jāparāda teikums, ka suns ēd.
# skriet – tai jāparāda teikums, ka suns skrien, notiekti izmantojot arī suņa vārdu
# izveido divus klases Suns objektus s1 un s2 un tiem izsauc abas metodes.
# piemēram,
# s1 = Suns("Reksis")
# s1.est() --- sagaidāmā izvade "Suns ēd"
# s1.skriet() --- sagaidāmā izvade "Reksis skrien"

print(f"{suns1.vards} šobrīd ēd")
print(f"{suns2.vards} ir sācis skriet!")