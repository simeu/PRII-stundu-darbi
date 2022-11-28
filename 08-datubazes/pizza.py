import PySimpleGUI as sg
import sqlite3

conn = sqlite3.connect("picas.db")
c = conn.cursor

picas = ["Margarita", "Toskāna", "Mafija", "Četri gadalaiki"]
izmeri = ["20", "30", "50", "60"]
klienti = ["Māris Briedis", "Krišs Matisons", "Ainārs Regressus", "Lotārs Mammietis"]
piegade = ["Bolt", "Wolt", "Cits kurjers", "Pakaļ-atnākšana"]  

def pasut_saraksts():  
    c.execute("SELECT pasutijumi FROM picas")
    razotaji = c.fetchall()
    print(razotaji)
    return razotaji


# pasūtījuma forma
layout1 = [
    [sg.Text("Picas izvēle:"), sg.Combo(values=picas, key="-PICA-PASUT-")],
    [sg.Text("Izmērs:"), sg.Combo(values=izmeri, key="-IZM-PASUT-")],
    [sg.Text("Klients:"), sg.Combo(values=klienti, key="-KLIENTS-PASUT-")],
    [sg.Text("Piegāde:"), sg.Combo(values=piegade, key="-PIEGADE-PASUT-")],
    [sg.Button("Pasūtīt", key = "-RADIT-"), sg.Button("Parādīt pasūtījumu(-s)")],
    [sg.HSep()],
    [sg.Text(key="-PASUTIJUMA-TEKSTS-")]
]

# picu, izmēru un piegādes veidu pārvaldības forma
layout2 = [
    [sg.Text("Picas nosaukums"), sg.Input(key="-JAUNS-NOSAUKUMS-")],
    [sg.Button("Saglabāt nosaukumu", key="-NOSAUKUMA-PIEVIENOSANA-")],
    [sg.HSep()],
    [sg.Text("Izmērs (cm)"), sg.Input(key="-JAUNS-IZMERS-")],
    [sg.Button("Saglabāt izmēru", key="-IZMERA-PIEVIENOSANA-")],
    [sg.HSep()],
    [sg.Text("Picas nosaukums"), sg.Combo(values=picas, key="-PICA-")],
    [sg.Text("Picas izmērs"), sg.Combo(values=izmeri, key="-IZMERS-")],
    [sg.Text("Picas cena"), sg.Input(key="-CENA-")],
    [sg.Button("Saglabāt picu", key="-PICAS-AR-CENU-PIEVIENOSANA-")],
    [sg.HSep()],
    [sg.Text("Piegādes veids"), sg.Input(key="-JAUNA-PIEGADE-")],
    [sg.Text("Piegādes cema"), sg.Input(key="-JAUNA-PIEGADE-CENA-")],
    [sg.Button("Saglabāt piegādi", key="-PIEGADES-PIEVIENOSANA-")],
    [sg.HSep()],
    [sg.Button("Poga bez eventa, lai kaut ko no tā visa parādītu. Izmantot pēc ieskatiem.")]
]

# Klientu pievienošana
layout3 = [
    [sg.Text("Vārds", size=14), sg.Input(key="-VARDS-")],
    [sg.Text("Tālrunis", size=14), sg.Input(key="-TALRUNIS-")],
    [sg.Text("Parole", size=14), sg.Input(key="-PAROLE-")],
    [sg.Button("Pievienot", size=14, key="-PIEVIENOT-KLIENTU-")],
    [sg.Button("Parādīt visus", key="-PARADIT-KLIENTUS-", size=14)],
    [sg.Text(key="-KLIENTA-INFO-")]
]

layout = [
    [sg.TabGroup([[sg.Tab("Picērija", layout1), sg.Tab("Pievienošana", layout2), sg.Tab("Klienti", layout3), ]])],
    [sg.Button("Iziet", size=12)]
]

window = sg.Window("PIZZA TIME", layout)

while True:
    event, values = window.read()

    if event == "Iziet" or event == sg.WINDOW_CLOSED:
        break

    if event == "Pasūtīt":
        pasutit = values["-PICA-PASUT-"]
        izm = values["-IZM-PASUT-"]
        klients = values["-KLIENTS-PASUT-"]
        piegade = values["-PIEGADE-PASUT-"]
        pasutijums = print(pasutit, izm, klients, piegade)
        pizzaDB = (pasutijums)
        c.execute("INSERT INTO pasutijumi (picas_ar_cenu, klienta_id, piegades_veids) VALUES (?,?,?)", (pizzaDB,))
        conn.commit()
        window.find_element("-RADIT-").update(values = pasut_saraksts())

    if event == "-PASUTIJUMA-TEKSTS-":
        c.execute("SELECT * FROM pasutijumi")
        txt = c.fetchall()
        for viens in txt:
            print(viens)

    if event == "-NOSAUKUMA-PIEVIENOSANA-":
        """
        "-JAUNS-NOSAUKUMS-"
        """
        pass

    if event == "-IZMERA-PIEVIENOSANA-":
        """
        "-JAUNS-IZMERS-"
        """
        pass

    if event == "-PICAS-AR-CENU-PIEVIENOSANA-":
        """
        "-PICA-"
        "-IZMERS-"
        "-CENA-" 
        """
        pass

    if event == "-PIEGADES-PIEVIENOSANA-":
        """
        "-JAUNA-PIEGADE-"
        "-JAUNA-PIEGADE-CENA-"
        """
        pass

    if event == "-PIEVIENOT-KLIENTU-":
        """
        "-VARDS-"
        "-TALRUNIS-"
        "-PAROLE-"
        """
        pass

    if event == "-PARADIT-KLIENTUS-":
        """
        "-KLIENTA-INFO-"
        """
        pass





window.close()

