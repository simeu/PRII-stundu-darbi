import PySimpleGUI as sg
import auto

# sg.theme_previewer()

izkartojums = [
[sg.Text("Marka")],
[sg.Input(key = "-MARKA-")],
[sg.Text("Modelis")],
[sg.Input(key = "-MODELIS-")],
[sg.Text("Cena")],
[sg.Input(key = "-CENA-")],
[sg.Text("Gads")],
[sg.Input(key = "-GADS-")],
[sg.Text("Nobraukums")],
[sg.Input(key = "-NOBRAUKUMS-")],
[sg.Button("Izveidot")],
[sg.Button("Iestatīt nosaukumu")]
]
izk = [
[sg.Text("Ievadītie dati")],
]

sg.theme("Black")
logs = sg.Window("Mašīnas", izkartojums)
while True:
    notikums, vertibas = logs.read()
    print(notikums, vertibas)
    if notikums == sg.WINDOW_CLOSED:
        break
    if notikums == "Izveidot":
        marka = vertibas["-MARKA-"]
        modelis = vertibas["-MODELIS-"]
        cena = vertibas["-CENA-"]
        gads = vertibas["-GADS-"]
        nobraukums = int(vertibas["-NOBRAUKUMS-"])

        masina = auto.Auto(marka, modelis, cena, gads, nobraukums)
        masina.paradit()

    if notikums == "Iestatīt nobraukumu":
        nobraukums = int(vertibas["-NOBRAUKUMS-"])
        masina.palielinat_nobraukumu(nobraukums)
        masina.paradit()





logs.close()