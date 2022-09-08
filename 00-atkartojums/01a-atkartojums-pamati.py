import math
# turpini programmu, lai tā parādītu mainīgo a un b summu, reizinājumu un dalījuma atlikumu
# vismaz vienai no rindām jābūt noformētai kā pilnam teikumam --- print(), print(f'')
# maini 1. un 2. rindas, lai mainīgo vērtības tiktu prasītas lietotājam --- input()
# Parādi stabiņā uz leju skaitļus no 1 līdz 5 ieskaitot --- for

a = int(input("Ievadi A skaitļa vērtību."))
b = int(input("Ievadi B skaitļa vērtību."))

print(f"A un B summa ir {a+b}.")
print(f"A un B reizinājums ir {a*b}.")
print(f"A un B dalījums ir {a//b}.")

skaitli = [1, 2, 3, 4, 5]
for viensSkaitlis in skaitli:
    print(f"{viensSkaitlis}")

# Parādi stabiņā uz leju masīva klases visus ierakstus
klases = ["12.a", "12.b", "12.c"]
nr = 1
for viensKlases in klases:
    print(f"{nr} {viensKlases}")
    nr = nr + 1

# Parādi no masīva klases tikai ierakstu ar vērtību 12.a --- []

# Noņem komentāra zīmi iepriekšējai rindai
# Ja, iedarbinot programmu, ievadītais vārds ir "nē", parādi ekrānā tekstu "Slepenais netika uzrakstīts"
# Visos citos gadījumos jāparāda teksts "Slepenais vārds ir" kopā ar ievadīto vārdu

atbilde = input("Uzraksti slepenu vārdu")

if atbilde == "nē":
    print("Slepenais netika atrasts")
else: 
    print(f"Slepenais vārds ir {atbilde}")



# Papilduzdevums: programma parāda tekstu "Slepenais vārds ir" un tik zvaigznītes, cik garš ir lietotāja ievadītais vārds