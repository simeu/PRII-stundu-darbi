# šie koda fragmenti vieni paši ir nestrādājoši. Paredzēti iekopēšani stundas gaitā datnē auto-gui-V5.py
import sqlite3
conn = sqlite3.connect("auto.db")
c = conn.cursor()

# 1. fragments
vaicajums = """
SELECT Razotaji.Nosaukums, Mashiinas.Modelis
FROM Mashiinas
INNER JOIN Razotaji  
ON Mashiinas.Razotaja_ID = Razotaji.ID
"""

c.execute(vaicajums)
transportlidzekli = c.fetchall()
print(transportlidzekli)

# 2. fragments
def razotaju_saraksts():
    c.execute("SELECT Nosaukums FROM Razotaji")
    razotaji = c.fetchall()
    return razotaji

# 3. fragments
window.find_element("-RAZOTAJI-").update(values = razotaju_saraksts())

# 4. fragments
razhotaaja_ID_SEL = f"SELECT ID FROM Razotaji WHERE Nosaukums LIKE \"{razotajs}\" "
c.execute(razhotaaja_ID_SEL)
razhotaaja_ID = c.fetchall()[0][0]

pievienosanai = (razhotaaja_ID, modelis, krasa, gads, nobraukums, cena)
c.execute("INSERT INTO Mashiinas (Razotaja_ID, Modelis, Krasa, Gads, Nobraukums, Cena) VALUES (?, ?, ?, ?, ?, ?)",
          pievienosanai)
conn.commit()

# 5. fragments
vaicajums = """
SELECT Darbinieki.Vards, Razotaji.Nosaukums, Mashiinas.Modelis, Salons.Veiktais_darbs
FROM Salons
INNER JOIN Mashiinas  
ON Mashiinas.ID = Salons.Auto_ID
INNER JOIN Razotaji
ON Mashiinas.Razotaja_ID = Razotaji.ID
INNER JOIN Darbinieki
ON Darbinieki.ID = Salons.Darbinieka_ID
"""

c.execute(vaicajums)
salons = c.fetchall()
print(salons)

# 6. fragments
def masinu_saraksts():
    vaicajums = """
    SELECT Mashiinas.ID, Razotaji.Nosaukums, Mashiinas.Modelis
    FROM Mashiinas
    INNER JOIN Razotaji  
    ON Mashiinas.Razotaja_ID = Razotaji.ID
    """
    c.execute(vaicajums)
    masinas = c.fetchall()

    masinas_salona_list = []
    for katrs in masinas:
        ieraksts = (' '.join(map(str, katrs)))
        masinas_salona_list.append(ieraksts)
    return masinas_salona_list

# 7. fragments
auto = values["-TRANSPORTLIDZEKLIS-"]
darbinieks = values["-DARBINIEKS-"]
darbs = values["-DARBS-"]
datums = values["-DATUMS-"]
ilgums = int(values["-ILGUMS-"])

auto_ID = int(auto.split(" ", 1)[0])
darbinieks_ID_SEL = f"SELECT ID FROM Darbinieki WHERE Vards LIKE \"{darbinieks}\" "

c.execute(darbinieks_ID_SEL)
darbinieka_ID = c.fetchall()[0][0]

pievienosanai = (auto_ID, darbinieka_ID, darbs, datums, ilgums)

c.execute("INSERT INTO Salons (Auto_ID, Darbinieka_ID, Veiktais_darbs, Datums, Ilgums) VALUES (?, ?, ?, ?, ?)", pievienosanai)
conn.commit()