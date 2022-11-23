import hashlib

parole = input("Raksti savu paroli")
parole_bin = str.encode(parole)
parole_hash = hashlib.sha256(parole_bin)
parole_hash_virkne = parole_hash.hexdigest()

print(parole_hash_virkne)