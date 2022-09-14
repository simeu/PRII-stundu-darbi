##################################
# Sazarojumi, cikli un funkcijas #
##################################
# 5. (2) Ekrānā 50 reizes parādi uzrakstu "Es nekad vairs negulēšu programmēšanas stundās".
# Šim uzdevumam jābūt kā funkcijai
def uzd5():
    nave = "Es nekad vairs negulēšu programmēšanas stundās."
    miegs = (nave*50)
    print(miegs)

uzd5()

# 6. (1) Ekrānā parādi skaitļus no 2 līdz 22 (ieskaitot)
def uzd6():
    for i in range(2, 23):
        num = i % 2
        if num > 0:
            print(f"{i} - nepāra")
        else:
            print(f"{i} - pāra")

uzd6()
# 7. (2) Papildini iepriekšējo kodu, lai skaitļiem blakus būtu uzraksts "pāra" vai "nepāra", 
# atkarībā no tā, kāds skaitlis tas ir