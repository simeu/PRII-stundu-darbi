import PySimpleGUI as sg

sagatave = [
    [sg.Text("Iespieddarba kategorija", size=25), sg.InputText(key="-KATEGORIJA-")],
    [sg.Text("Iespieddarba nosaukums", size=25), sg.InputText(key="-NOSAUKUMS-")],
    [sg.Text("Iespieddarba autors", size=25), sg.InputText(key="-AUTORS-")],
    [sg.Text("Izdevums pieejams", size=25), sg.InputText(key="-PIEJAMS-")],
    [sg.Text("Lasītāja vārds", size=25), sg.InputText(key="-VARDS-")],
    [sg.Text("Lasītāja uzvārds", size=25), sg.InputText(key="-UZVARDS-")],
    [sg.Text("Lasītāja pk", size=21), sg.InputText(key="-PK-")],
    [sg.Text("Lasītāja tel nr", size=21), sg.InputText(key="-TEL-")],
    [sg.Text("Izsniegšanas datums", size=25), sg.InputText(key="-DATUMS-")],
    [sg.Text("Izsniegšanas termiņš", size=25), sg.InputText(key="-TERMINS-")],
    [sg.Text("Atgriešanas datums", size=25), sg.InputText(key="-ATGRIESANAS-")],
    [sg.Text(key = "-APRAKSTS-")],
    [sg.Button("Izveidot ierakstu", size=25, key="-IZVEIDOT-")]
]


# Zemāk dotos layout papildini ar sagataves elementiem atbilstoši Tavam DB plānojumam.
# Ja nepieciešams, pievieno jaunus.
layout1 = [

]

layout2 = [

]

# Maini izkārtojumu atbilstoši iepriekš izveidotajam
layout = [
    [sg.TabGroup([[sg.Tab("1. sadaļa", layout1), sg.Tab("2. sadaļa", layout2)]])]

]

window = sg.Window("Bibliotēka", layout)

while True:
    event, values = window.read()
    """
    ["-KATEGORIJA-"]
    ["-NOSAUKUMS-"]
    ["-AUTORS-"]
    ["-PIEJAMS-"]
    ["-VARDS-"]
    ["-UZVARDS-"]
    ["-PK-"]
    ["-TEL-"]
    ["-DATUMS-"]
    ["-TERMINS-"]
    ["-ATGRIESANAS-"]    
    """


    if event == sg.WIN_CLOSED:
        break

    if event == "-IZVEIDOT-":
        pass


window.close()