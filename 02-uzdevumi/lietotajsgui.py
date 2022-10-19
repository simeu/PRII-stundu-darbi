import PySimpleGUI as sg
import lietotaajs as li
from fpdf import FPDF

sg.theme("Black")

izvl = [
    ["File", ["Saglabāt kā JSON", "Saglabāt kā PDF"]],
    ["Help", ["About", "Support"]]
]
izk1 = [
[sg.Text("Laipni lugts musu nezinamajā portala!")],
[sg.Text("Ievadiet savu lietotajvardu"), sg.Input(key = "-USER-")],
[sg.Text("Ievadiet savu vardu un uzvardu"), sg.Input(key = "-USER2-")],
[sg.Text("Ievadiet savu vecumu"), sg.Input(key = "-T-")],
[sg.Text("Ievadiet savu izveleto valodu"), sg.Input(key = "-P-")],
[sg.Button("OK"), sg.Text(key = "-X-")],
[sg.Button("Reģistrēt"), sg.Text(key = "-Z-")],
[sg.Button("Iziet"), sg.Text(key = "-M-")],]

izk2 = [[sg.Button("Saglabāt kā JSON", size = 12)]]

izk3 = [[sg.Button("Saglabāt kā PDF", size = 12)]]

izk4 = [
    [sg.Button("Apraksts", size = 12)]
]
izkartojums = [
    [sg.Menu(izvl)],
    [sg.TabGroup([[sg.Tab("Ievade", izk1)],[sg.Tab("Saglabāt kā JSON", izk2)],[sg.Tab("Saglabāt kā PDF", izk3)], sg.Tab("Apraksts", izk4)])]

]

logs = sg.Window("Nezināmās programmas ierakstīšanās", izkartojums)
while True:
    notikums, vertibas = logs.read()
    if notikums == sg.WINDOW_CLOSED:
        break
    if notikums == "OK":
        print("Ierakstīšanās veiksmīga!")
        logs.close()
    if notikums == "Reģistrēt":
        vards = vertibas["-USER-"]
        uzvards = vertibas["-USER2-"]
        vecums = vertibas["-T-"]
        valoda = vertibas["-P-"]
        lietotajs = li.Lietotajs(vards, uzvards, vecums, valoda)
        lietotajs.sasveicinies()
        print("Dati reģistrēti")

    if notikums == "Iziet":
        logs.close()

    if notikums == "Saglabāt kā JSON":
        lietotajs.veido_vardnicu()
        lietotajs.saglabat_json()
        lietotajs.sasveicinies()

    if notikums == "Saglabāt kā PDF":
        lietotajs.veido_vardnicu()
        lietotajs.saglabat_pdf() # Rāda error'u "Lietotajs is not defined", kaut vai ja tas ir definēts.
        lietotajs.sasveicinies()

    if notikums == "About":
        sg.popup("Hello, World!")
        if notikums == "OK":
            logs.close
