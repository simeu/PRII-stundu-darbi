# Dota datubāze biblioteka.db
# Izveido savienojumu un kursoru
import sqlite3
conn = sqlite3.connect("biblioteka.db")
c = conn.cursor()

# No datu bāzes parādi visus tabulas Lasitaji ierakstus
def radit():
    c.execute("SELECT * from biblioteka")
    rezultats = c.fetchall()
    for viens in rezultats:
        print(viens)

# Izveido jaunu datubāzes tabulu Pakalpojumi
# ar šādiem laukiem: id, nosaukums, maksa
c.execute("CREATE TABLE IF NOT EXISTS Pakalpojumi (Id INTEGER PRIMARY KEY AUTOINCREMENT, Nosaukums TEXT, maksa REAL)")
conn.commit()

# Tabulai Pakalpojumi pievieno ierakstu pakalpojumu "skenēšana" ar cenu "0,50"
skenesana = ("skenēšana", "0.5")
c.execute("INSERT INTO Pakalpojumi(nosaukums, maksa) VALUES (?, ?)", skenesana)

# Saglabā izmaiņas DB un slēdz savienojumu
def saglabashana():
    conn.commit()
    c.close()
    conn.close()

saglabashana()