import PySimpleGUI as sg
import sqlite3
import hashlib

conn = sqlite3.connect("noma.db")
c = conn.cursor()

def instrumentu_veidi():
    vaic = "SELECT veids FROM Instruments"
    c.execute(vaic)
    i = c.fetchall()
    instrumenti = []
    for viens in i:
        instrumenti.append(viens[0])
    return instrumenti

def klients():
    vaica = "SELECT * FROM Klients"
    c.execute(vaica)
    kl = c.fetchall
    klienti = []
    for divi in kl:
        klienti.append(divi[0])
    return klienti

def nomasinfo():
    vaicaj = "SELECT * FROM Cenas"
    c.execute(vaicaj)
    nomas = []
    for tris in nomas:
        nomas.append(tris[0])
    return nomas


instruments = instrumentu_veidi()
klient = klients()
noma = nomasinfo()

layout1 = [
    [sg.Text("Laipni lūgts Kārļa celtniecības rīku nomā! Problēmu situācijas gadījumā zvanat uz numuru: +371 21234567.")],
    [sg.Text("Izvēlieties instrumenta veidu."), sg.Combo(values = instruments, key = "-I-")],
    [sg.Text("Izvēlieties nomas sākumdatumu (pierakstīt formātā: dd.mm.gggg)."), sg.InputText(values = noma, key = "-D-")],
    [sg.Text("Izvēlies nomas beigu datumu (šo vienmēr var vēlāk pagarināt).", sg.Input(key = "-B-"))],
    [sg.Text("Ievadi savu vārdu."), sg.InputText(key = "-V-")],
    [sg.Text("Ievadi savu uzvārdu."), sg.InputText(key = "-U-")],
    [sg.Text("Ievadi savu tālruņa numuru."), sg.Input(key = "-N-")],
    [sg.Text("Ievadi savu paroli (Nav obligāti.)."), sg.Input(key = "-P-")]
]
layout2 = [
]

layout = [
    [sg.TabGroup([[sg.Tab("Jauna Noma", layout1), sg.Tab("Klients", layout2)]])]
]

window = sg.Window("Noma", layout)

while True:
    event, values = window.read()
    if event == "-I-":
        instrumenti = values["-I-"]
        window.find_element("-").update(values=instrumentu_veidi())
    if event == "-D-":
        values["-D-"]

    if event == "-B-":
        beigas = values["-B-"]



    if event == "-V-":
        vards = values["-V-"]
        uzvards = values["-U-"]
        telefons = values["-N-"]
        parole = values["-P-"]
        parole_b = str.encode(parole)
        parole_c = hashlib.sha512(parole_b)
        parole_d = parole_c.hexdigest()
        klientsDB = (vards, uzvards, telefons, parole_d)
        c.execute("INSERT INTO Klients (vards, uzvards, telefons, parole_d) VALUES (?, ?, ?)", klientsDB)
        conn.commit







    """
    ["-KATEGORIJA-"]
    ["-NOSAUKUMS-"]
    ["-RAKSTUROJUMI-"]
    ["-CENA-"]
    ["-PIEJAMS-"]
    ["-SAKUMS-"]
    ["-BEIGAS-"]
    """

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-SAGLABAT-":
        pass



window.close()
conn.commit()
c.close()
conn.close()
