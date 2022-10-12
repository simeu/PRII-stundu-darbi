import PySimpleGUI as sg
import lietotaajs as li

sg.theme("Black")

izkartojums = [
[sg.Text("Laipni lūgts mūsu nezināmajā portālā!")],
[sg.Text("Ievadiet savu lietotājvārdu"), sg.Input(key = "-USER-")],
[sg.Text("Ievadiet savu vecumu"), sg.Input(key = "-T-")],
[sg.Text("Ievadiet savu izvēlēto valodu"), sg.Input(key = "-P-")],
[sg.Button("OK"), sg.Text(key = "-X-")],
[sg.Button("Reģistrēt"), sg.Text(key = "-Z-")],
[sg.Button("Iziet"), sg.Text(key = "-M-")]
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
        vecums = vertibas["-T-"]
        valoda = vertibas["-P-"]

        lietotajs = li.Lietotajs(vards, vecums, valoda)
        lietotajs.paradit()
        print("Dati reģistrēti")

    if notikums == "Iziet":
        logs.close()

