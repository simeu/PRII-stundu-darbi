import hashlib

parole = input("Ieraksti vārdu Lāčplēsis")
parole_bin = str.encode(parole)
parole_hash = hashlib.md5(parole_bin)
parole_hash_virkne = parole_hash.hexdigest()

print(parole_hash_virkne)

