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
c.execute("CREATE TABLE IF NOT EXISTS pakalpojumi (Id INTEGER, Nosaukums TEXT, Maksa INTEGER)")

# Tabulai Pakalpojumi pievieno ierakstu pakalpojumu "skenēšana" ar cenu "0,50"

c.execute("INSERT INTO biblioteka(7, skenēšana, 0,50) VALUES (?, ?, ?)")

# Saglabā izmaiņas DB un slēdz savienojumu
def saglabashana():
    conn.commit()
    c.close()
    conn.close()