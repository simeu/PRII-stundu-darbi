import PySimpleGUI as sg
from autoV5 import Auto
from darbinieksV5 import Darbinieks
import sqlite3
import hashlib

conn = sqlite3.connect("auto.db")
c = conn.cursor()

def razotaju_saraksts():
    c.execute("SELECT Nosaukums FROM Razotaji")
    razotaji = c.fetchall()
    return razotaji



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

mashiinas = masinu_saraksts()
razotaji = razotaju_saraksts()
krasas = ["Melna", "Balta"]

# ražotāji
layout1 = [
    [sg.Text("Marka", size=14)],
    [sg.Input(key="-MARKA-")],
    [sg.Button("Pievienot", size=14, key="-PIEVIENOT-MARKU-")],
    [sg.Button("Parādīt visas", key="-PARADIT-MARKAS-", size=14)]
]

# salona darbinieki
layout2 = [
    [sg.Text("Vārds", size=14), sg.Input(key="-VARDS-")],
    [sg.Text("Amats", size=14), sg.Input(key="-AMATS-")],
    [sg.Text("Parole", size=14), sg.Input(key="-PAROLE-")],
    [sg.Button("Pievienot", size=14, key="-PIEVIENOT-DARBINIEKU-")],
    [sg.Button("Parādīt visus", key="-PARADIT-DARBINIEKUS-", size=14)]
]

# transportlīdzekļi
layout3 = [
    [sg.Text("Ražotājs", size=14), sg.Combo(values=razotaji, key="-RAZOTAJI-")],
    [sg.Text("Modelis", size=14), sg.Input(key = "-MODELIS-")],
    [sg.Text("Krāsa", size=14), sg.Combo(values=krasas, key="-KRASA-")],
    [sg.Text("Gads", size=14), sg.Input(key = "-GADS-")],
    [sg.Text("Nobraukums", size=14), sg.Input(key = "-NOBRAUKUMS-")],
    [sg.Text("Cena", size=14), sg.Input(key = "-CENA-")],
    [sg.Button("Saglabāt", size=14, key="-PIEVIENOT-TRANSPORTLIDZEKLI-")],
    [sg.Button("Parādīt visus", size=14, key="-PARADIT-TRANSPORTLIDZEKLUS-")]
]

# salona darbs
layout4 = [
    [sg.Text("Auto", size=12), sg.Combo(values = mashiinas, key="-TRANSPORTLIDZEKLIS-")],
    # [sg.Text("Auto", size=12), sg.Input(key="-TRANSPORTLIDZEKLIS-")],
    # [sg.Text("Darbinieks", size=12), sg.Combo(key="-DARBINIEKS-")],
    [sg.Text("Darbinieks", size=12), sg.Input(key="-DARBINIEKS-")],
    [sg.Text("Veiktais darbs", size=12), sg.Input(key = "-DARBS-")],
    [sg.Text("Datums", size=12), sg.Input(key = "-DATUMS-")],
    [sg.Text("Ilgums", size=12), sg.Input(key = "-ILGUMS-")],
    [sg.Button("Saglabāt", size=12, key="-SAGLABAT-SALONS-")],
    [sg.Button("Parādīt visas", size=18, key="-PARADIT-SALONU-")]
]

# Apraksts. Pagaidām netiek rādīts un izmantots.
layout5 = [
    [sg.Text(key = "-APRAKSTS-")]
]

layout = [
    [sg.TabGroup([[sg.Tab("Markas", layout1), sg.Tab("Darbinieki", layout2), sg.Tab("Transportlīdzekļi", layout3), sg.Tab("Salons", layout4), sg.Tab("Apraksts", layout5, visible=False)]])],
    [sg.Button("Iziet", size=12)]
]

window = sg.Window("Auto", layout)

while True:
    event, values = window.read()
    # print(event, values)

    if event == "Iziet" or event == sg.WINDOW_CLOSED:
        break

    if event == "-PIEVIENOT-MARKU-":
        razotajs = values["-MARKA-"]
        print(razotajs)
        markaDB = razotajs
        c.execute("INSERT INTO Razotaji (Nosaukums) VALUES (?)", (markaDB,))
        conn.commit()
        window.find_element("-RAZOTAJI-").update(values = razotaju_saraksts())


    if event == "-PARADIT-MARKAS-":
        c.execute("SELECT * FROM Razotaji")
        #c.execute("SELECT Nosaukums FROM Razotaji")
        razotaji = c.fetchall()
        for viens in razotaji:
            print(viens)

    if event == "-PIEVIENOT-DARBINIEKU-":
        vards = values["-VARDS-"]
        amats = values["-AMATS-"]
        parole = values["-PAROLE-"]

        parole_bin = str.encode(parole)
        parole_sha256 = hashlib.sha256(parole_bin)
        print(parole_sha256)
        parole_hash = parole_sha256.hexdigest()

        darbinieks = Darbinieks(vards, amats, parole_hash)
        darbinieks.paradit_darbinieku()

        darbinieksDB = (vards, amats, parole_hash)
        c.execute("INSERT INTO Darbinieki (Vards, Amats, Parole) VALUES (?, ?, ?)", darbinieksDB)
        conn.commit()

    if event == "-PARADIT-DARBINIEKUS-":
        c.execute("SELECT * FROM Darbinieki")
        darbinieki = c.fetchall()
        for viens in darbinieki:
            print(viens)

    if event == "-PIEVIENOT-TRANSPORTLIDZEKLI-":
        razotajs = values["-RAZOTAJI-"][0]
        modelis = values["-MODELIS-"]
        krasa = values["-KRASA-"]
        gads = values["-GADS-"]
        nobraukums = values["-NOBRAUKUMS-"]
        cena = values["-CENA-"]
        auto = Auto(razotajs, modelis, krasa, gads, nobraukums, cena)
        auto.paradit()

        razhotaaja_ID_SEL = f"SELECT ID FROM Razotaji WHERE Nosaukums LIKE \"{razotajs}\" "
        c.execute(razhotaaja_ID_SEL)
        razhotaaja_ID = c.fetchall()[0][0]

        pievienosanai = (razhotaaja_ID, modelis, krasa, gads, nobraukums, cena)
        c.execute("INSERT INTO Mashiinas (Razotaja_ID, Modelis, Krasa, Gads, Nobraukums, Cena) VALUES (?, ?, ?, ?, ?, ?)",
            pievienosanai)
        conn.commit()

    if event == "-PARADIT-TRANSPORTLIDZEKLUS-":
        vaicajums = """
        SELECT Razotaji.Nosaukums, Mashiinas.Modelis
        FROM Mashiinas
        INNER JOIN Razotaji  
        ON Mashiinas.Razotaja_ID = Razotaji.ID
        """

        c.execute(vaicajums)
        transportlidzekli = c.fetchall()
        print(transportlidzekli)

    if event == "-SAGLABAT-SALONS-":
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

    if event == "-PARADIT-SALONU-":
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



window.close()